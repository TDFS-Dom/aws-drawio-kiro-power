#!/bin/bash
# Export all pages from all .drawio files in draw-patterns/ to PNG
# Requires: draw.io Desktop installed at /Applications/draw.io.app

DRAWIO="/Applications/draw.io.app/Contents/MacOS/draw.io"
INPUT_DIR="draw-patterns"
OUTPUT_DIR="draw-patterns/exports"

mkdir -p "$OUTPUT_DIR"

for file in "$INPUT_DIR"/*.drawio; do
    if [ ! -f "$file" ]; then continue; fi
    
    basename=$(basename "$file" .drawio)
    slug=$(echo "$basename" | tr ' ' '_' | tr '[:upper:]' '[:lower:]')
    
    # Count pages
    page_count=$(grep -c 'diagram name=' "$file")
    echo "=== $basename ($page_count pages) ==="
    
    for ((i=0; i<page_count; i++)); do
        output_file="$OUTPUT_DIR/${slug}_page${i}.png"
        echo "  Page $i → $output_file"
        "$DRAWIO" --export --format png --page-index "$i" --scale 2 --border 10 --output "$output_file" "$file" 2>/dev/null
    done
done

echo ""
echo "✅ Done. Exported to $OUTPUT_DIR/"
ls "$OUTPUT_DIR"/*.png 2>/dev/null | wc -l
echo "files"
