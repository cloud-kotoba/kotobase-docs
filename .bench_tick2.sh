#!/bin/sh
DOC=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md
OUT=/tmp/bench_tick2.out
echo "=== NEXT lines ===" > "$OUT"
grep -n "NEXT" "$DOC" >> "$OUT"
echo "=== K-Z3 lines ===" >> "$OUT"
grep -n "K-Z3" "$DOC" >> "$OUT"
echo "=== Iteration log header ===" >> "$OUT"
grep -n "^## Iteration log" "$DOC" >> "$OUT"
echo "=== total lines ===" >> "$OUT"
wc -l "$DOC" >> "$OUT"
echo "=== DONE ===" >> "$OUT"