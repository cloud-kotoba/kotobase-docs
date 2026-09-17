#!/bin/sh
DOC=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md
OUT=/tmp/bench_tick3.out
echo "=== scratch run468 files ===" > "$OUT"
ls -la /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b468* 2>&1 >> "$OUT"
echo "=== diff HEAD query-cosientist.md (empty=clean) ===" >> "$OUT"
git -C /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs diff HEAD -- query-cosientist.md | wc -l >> "$OUT"
echo "=== run468 grep in doc (evidence presence count) ===" >> "$OUT"
grep -c "run468" "$DOC" >> "$OUT"
echo "=== run467 presence count ===" >> "$OUT"
grep -c "run467" "$DOC" >> "$OUT"
echo "=== K-Z3 row line numbers ===" >> "$OUT"
grep -n "^| K-Z3 " "$DOC" >> "$OUT"
echo "=== last iter-log entry line (first line after header) ===" >> "$OUT"
grep -n "^## Iteration log" "$DOC" >> "$OUT"
echo "=== DONE ===" >> "$OUT"