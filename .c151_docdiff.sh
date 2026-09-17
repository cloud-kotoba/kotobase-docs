#!/bin/sh
OUT=.c151_docdiff.txt
: > "$OUT"
echo "=== git status (short) ===" >> "$OUT"
git status --short >> "$OUT" 2>&1
echo "=== diff query-cosientist.md vs HEAD (first 80 lines) ===" >> "$OUT"
git diff HEAD -- query-cosientist.md | head -80 >> "$OUT" 2>&1
echo "=== diff stat ===" >> "$OUT"
git diff --stat HEAD -- query-cosientist.md >> "$OUT" 2>&1
echo "=== mtime of doc ===" >> "$OUT"
ls -la --time-style=full-iso query-cosientist.md 2>/dev/null >> "$OUT" || ls -laT query-cosientist.md >> "$OUT" 2>&1
echo "=== where does run518 appear ===" >> "$OUT"
grep -n 'run518' query-cosientist.md >> "$OUT" 2>&1