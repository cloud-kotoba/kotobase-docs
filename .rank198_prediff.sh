#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank198_prediff.out
: > "$OUT"
echo "===NUMSTAT===" >> "$OUT"; git diff HEAD --numstat -- query-cosientist.md >> "$OUT" 2>&1
echo "===STAT===" >> "$OUT"; git diff HEAD --stat -- query-cosientist.md >> "$OUT" 2>&1
echo "===HEADER-COUNT===" >> "$OUT"; git diff HEAD -- query-cosientist.md | grep -c '^## Iteration log' >> "$OUT" 2>&1
echo "===SHOW-HEADER-HEAD===" >> "$OUT"; git show HEAD:query-cosientist.md | grep -c '^## Iteration log' >> "$OUT" 2>&1
echo "===SHOW-HEADER-WT===" >> "$OUT"; grep -c '^## Iteration log' query-cosientist.md >> "$OUT" 2>&1
echo done