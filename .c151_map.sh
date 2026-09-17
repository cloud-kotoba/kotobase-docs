#!/bin/sh
OUT=.c151_map.txt
: > "$OUT"
echo "=== run519 occurrences (0 = free) ===" >> "$OUT"
grep -c 'run519' query-cosientist.md >> "$OUT" 2>&1
grep -n 'run519' query-cosientist.md >> "$OUT" 2>&1
python3 .c151_l279.py
echo "python_rc=$?" >> "$OUT"