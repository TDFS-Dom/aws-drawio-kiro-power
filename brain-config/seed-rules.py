"""
Brain Seed — Parse drawio-master rules and insert into SQLite FTS5.

Direct DB access (no server needed). Creates tables if not exist.
"""

import sys
import os
import re
import sqlite3
import hashlib
import time
import json

def init_db(db_path):
    """Initialize brain DB with required schema."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    db = sqlite3.connect(db_path)
    db.execute("PRAGMA journal_mode = WAL")
    db.execute("PRAGMA foreign_keys = ON")

    db.executescript("""
        CREATE TABLE IF NOT EXISTS lambda_memories (
            hash            TEXT PRIMARY KEY,
            created_at      INTEGER NOT NULL,
            last_accessed   INTEGER NOT NULL,
            access_count    INTEGER NOT NULL DEFAULT 0,
            importance      REAL NOT NULL DEFAULT 1.0,
            explicit_save   INTEGER NOT NULL DEFAULT 0,
            full_text       TEXT NOT NULL,
            summary_text    TEXT NOT NULL,
            essence_text    TEXT NOT NULL,
            context_log     TEXT,
            tags            TEXT NOT NULL DEFAULT '[]',
            memory_type     TEXT NOT NULL DEFAULT 'conversation',
            sensitivity     TEXT NOT NULL DEFAULT 'public',
            project         TEXT DEFAULT NULL,
            session_id      TEXT NOT NULL,
            owner_id        TEXT DEFAULT 'default',
            embedding       BLOB DEFAULT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_memories_project
            ON lambda_memories(project);
        CREATE INDEX IF NOT EXISTS idx_memories_importance
            ON lambda_memories(importance DESC);
        CREATE INDEX IF NOT EXISTS idx_memories_last_accessed
            ON lambda_memories(last_accessed DESC);
        CREATE INDEX IF NOT EXISTS idx_memories_owner
            ON lambda_memories(owner_id);

        CREATE VIRTUAL TABLE IF NOT EXISTS lambda_memories_fts
        USING fts5(
            summary_text, essence_text, tags,
            content='lambda_memories', content_rowid='rowid'
        );

        CREATE TRIGGER IF NOT EXISTS lambda_memories_ai AFTER INSERT ON lambda_memories BEGIN
            INSERT INTO lambda_memories_fts(rowid, summary_text, essence_text, tags)
            VALUES (new.rowid, new.summary_text, new.essence_text, new.tags);
        END;

        CREATE TRIGGER IF NOT EXISTS lambda_memories_ad AFTER DELETE ON lambda_memories BEGIN
            INSERT INTO lambda_memories_fts(lambda_memories_fts, rowid, summary_text, essence_text, tags)
            VALUES ('delete', old.rowid, old.summary_text, old.essence_text, old.tags);
        END;

        CREATE TRIGGER IF NOT EXISTS lambda_memories_au AFTER UPDATE ON lambda_memories BEGIN
            INSERT INTO lambda_memories_fts(lambda_memories_fts, rowid, summary_text, essence_text, tags)
            VALUES ('delete', old.rowid, old.summary_text, old.essence_text, old.tags);
            INSERT INTO lambda_memories_fts(rowid, summary_text, essence_text, tags)
            VALUES (new.rowid, new.summary_text, new.essence_text, new.tags);
        END;
    """)

    return db


def make_hash(content):
    """Generate unique hash for a memory entry."""
    return hashlib.sha256(f"{int(time.time())}:{content[:100]}".encode()).hexdigest()[:16]


def store_memory(db, content, summary, essence, importance, tags, project="drawio-master"):
    """Insert a memory into the brain DB."""
    now = int(time.time())
    h = make_hash(content)

    db.execute("""
        INSERT OR REPLACE INTO lambda_memories
        (hash, created_at, last_accessed, access_count, importance,
         explicit_save, full_text, summary_text, essence_text, context_log,
         tags, memory_type, sensitivity, project, session_id, owner_id)
        VALUES (?, ?, ?, 0, ?, 1, ?, ?, ?, NULL, ?, 'knowledge', 'public', ?, ?, 'default')
    """, (h, now, now, importance, content, summary, essence,
          json.dumps(tags), project, f"seed_{now}"))

    # Small delay to ensure unique hashes
    time.sleep(0.01)
    return h


def parse_rules_by_section(filepath):
    """Parse a markdown file into sections (## or ### headers)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = []
    current_title = ""
    current_body = []

    for line in content.split('\n'):
        if line.startswith('## ') or line.startswith('### '):
            if current_title and current_body:
                sections.append({
                    'title': current_title,
                    'body': '\n'.join(current_body).strip()
                })
            current_title = line.lstrip('#').strip()
            current_body = []
        else:
            current_body.append(line)

    # Last section
    if current_title and current_body:
        sections.append({
            'title': current_title,
            'body': '\n'.join(current_body).strip()
        })

    return sections


def extract_tags_from_title(title):
    """Extract relevant tags from section title."""
    tags = []
    title_lower = title.lower()

    tag_map = {
        'edge': ['edge', 'line', 'arrow', 'flow', 'connection'],
        'routing': ['routing', 'waypoint', 'path', 'route', 'bypass'],
        'anti-pattern': ['anti-pattern', 'violation', 'ap-', '❌'],
        'cross-account': ['cross-account', 'cross-container', 'intermediate'],
        'geometry': ['geometry', 'spacing', 'size', 'width', 'height', 'padding'],
        'icon': ['icon', 'service', 'resicon', 'shape'],
        'validation': ['check', 'validation', 'verify', 'checklist'],
        'style': ['style', 'container', 'group', 'color', 'stroke'],
        'security': ['security', 'kms', 'guardduty', 'iam', 'waf'],
        'networking': ['networking', 'vpc', 'tgw', 'transit', 'dns'],
        'algorithm': ['algorithm', 'pathfinding', 'calculate', 'function'],
        'fan-in': ['fan-in', 'fan-out', 'merge', 'bundle', 'parallel'],
        'trunk': ['trunk', 'vertical', 'corridor', 'lane'],
        'dashed': ['dashed', 'dependency', 'encryption', 'kms'],
    }

    for tag, keywords in tag_map.items():
        if any(kw in title_lower for kw in keywords):
            tags.append(tag)

    return tags if tags else ['general']


def generate_summary(title, body):
    """Generate a concise summary from section content."""
    # Take first non-empty, non-code line as summary
    lines = [l.strip() for l in body.split('\n')
             if l.strip() and not l.strip().startswith('```')
             and not l.strip().startswith('|')
             and not l.strip().startswith('-')
             and not l.strip().startswith('#')]

    summary = f"{title}: {lines[0]}" if lines else title
    return summary[:200]


def generate_essence(title):
    """Generate ultra-short essence (keywords) from title."""
    # Remove special chars, keep meaningful words
    words = re.sub(r'[^a-zA-Z0-9\s\-]', '', title).split()
    return ' '.join(words[:8])


def determine_importance(title, body):
    """Score importance 3-5 based on content signals."""
    title_lower = title.lower()

    # Importance 5: critical rules, anti-patterns, mandatory
    if any(kw in title_lower for kw in ['mandatory', 'critical', '🚨', 'anti-pattern', 'ap-', 'violation']):
        return 5
    if 'PHẢI' in body[:200] or 'BẮT BUỘC' in body[:200] or 'NEVER' in body[:200]:
        return 5

    # Importance 4: specific patterns, algorithms, edge types
    if any(kw in title_lower for kw in ['algorithm', 'pathfinding', 'case', 'e1', 'pattern']):
        return 4
    if re.search(r'E\d+[a-z]?\b', title):  # E12, E16, E12b etc.
        return 4

    # Importance 3: reference, catalog, general info
    return 3


# ─── Main ───────────────────────────────────────────────────

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 seed-rules.py <refs_dir> <db_path>")
        sys.exit(1)

    refs_dir = sys.argv[1]
    db_path = sys.argv[2]

    print(f"📂 References: {refs_dir}")
    print(f"💾 Database: {db_path}")

    db = init_db(db_path)

    # Clear existing drawio-master memories (re-seed)
    deleted = db.execute(
        "DELETE FROM lambda_memories WHERE project = 'drawio-master'"
    ).rowcount
    if deleted:
        print(f"🗑  Cleared {deleted} existing drawio-master memories")

    # Files to ingest
    rule_files = [
        'line-drawing-rules.md',
        'aws-icons.md',
        'draw-patterns.md',
        'shared-standards.md',
        'validation-rules.md',
    ]

    # Check for optional files
    optional_files = ['geometry-rules.md', 'style-guide.md', 'architecture-patterns.md']
    for f in optional_files:
        if os.path.exists(os.path.join(refs_dir, f)):
            rule_files.append(f)

    total_stored = 0

    for filename in rule_files:
        filepath = os.path.join(refs_dir, filename)
        if not os.path.exists(filepath):
            print(f"⚠️  Skip (not found): {filename}")
            continue

        sections = parse_rules_by_section(filepath)
        stored = 0

        for section in sections:
            # Skip very short sections (headers without content)
            if len(section['body']) < 50:
                continue

            # Chunk large sections (>2000 chars)
            body = section['body']
            if len(body) > 2000:
                # Split by sub-sections or paragraphs
                chunks = re.split(r'\n(?=###|\n\n)', body)
                for i, chunk in enumerate(chunks):
                    if len(chunk.strip()) < 50:
                        continue
                    chunk_title = f"{section['title']} (part {i+1})"
                    tags = extract_tags_from_title(section['title'])
                    tags.append(filename.replace('.md', ''))
                    summary = generate_summary(chunk_title, chunk)
                    essence = generate_essence(section['title'])
                    importance = determine_importance(section['title'], chunk)

                    store_memory(db, chunk.strip(), summary, essence, importance, tags)
                    stored += 1
            else:
                tags = extract_tags_from_title(section['title'])
                tags.append(filename.replace('.md', ''))
                summary = generate_summary(section['title'], body)
                essence = generate_essence(section['title'])
                importance = determine_importance(section['title'], body)

                store_memory(db, body, summary, essence, importance, tags)
                stored += 1

        print(f"✅ {filename}: {stored} memories stored")
        total_stored += stored

    db.commit()
    db.close()

    print(f"\n📊 Total: {total_stored} memories seeded for project 'drawio-master'")


if __name__ == '__main__':
    main()
