#!/bin/bash
DOC=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md
OUT=/tmp/kb_iter.txt
echo "=== iter log header line ===" > "$OUT"
grep -n "## Iteration log" "$DOC" >> "$OUT" 2>&1
echo "=== total lines ===" >> "$OUT"
wc -l "$DOC" >> "$OUT" 2>&1
echo "=== NEXT occurrences (last 10) ===" >> "$OUT"
grep -n "NEXT" "$DOC" | tail -10 >> "$OUT" 2>&1
echo "=== K-Z3 row line ===" >> "$OUT"
grep -n "| K-Z3 | worker |" "$DOC" >> "$OUT" 2>&1
echo "done"