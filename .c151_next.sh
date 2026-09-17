#!/bin/sh
OUT=.c151_next.txt
: > "$OUT"
echo "=== lines containing run520 ===" >> "$OUT"
grep -n 'run520' query-cosientist.md | head -5 >> "$OUT" 2>&1
echo "=== current iter-log top 3 entries (first 140 chars each) ===" >> "$OUT"
python3 .c151_top3.py >> "$OUT" 2>&1