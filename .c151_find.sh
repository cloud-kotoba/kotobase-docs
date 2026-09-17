#!/bin/sh
OUT=.c151_find.txt
: > "$OUT"
echo "=== run516 / run517 evidence occurrences before iter-log (lines <408) ===" >> "$OUT"
awk 'NR<408 && /run516|run517/{print NR": "substr($0,1,200)}' query-cosientist.md >> "$OUT" 2>&1
echo "=== last K-Z3 evidence line numbers (search run515..517) ===" >> "$OUT"
grep -n 'run51[5-8]' query-cosientist.md | head -20 >> "$OUT" 2>&1
echo "=== total lines & iter-log header line ===" >> "$OUT"
grep -n '## Iteration log' query-cosientist.md >> "$OUT" 2>&1
wc -l query-cosientist.md >> "$OUT" 2>&1