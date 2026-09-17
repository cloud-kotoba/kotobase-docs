#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank_refetch.out
: > "$OUT"
echo "===FETCH-net===" >> "$OUT"; git fetch net-kotobase 2>&1 | head -5 >> "$OUT"
echo "===FETCH-bench===" >> "$OUT"; git fetch bench_fetch 2>&1 | head -5 >> "$OUT"
echo "===HEAD===" >> "$OUT"; git rev-parse HEAD >> "$OUT" 2>&1
echo "===net-main===" >> "$OUT"; git rev-parse net-kotobase/main >> "$OUT" 2>&1
echo "===bench-main===" >> "$OUT"; git rev-parse bench_fetch/main >> "$OUT" 2>&1
echo "===DIFF-query===" >> "$OUT"; git diff HEAD --stat -- query-cosientist.md >> "$OUT" 2>&1
echo "===DIFF-numstat===" >> "$OUT"; git diff HEAD --numstat -- query-cosientist.md >> "$OUT" 2>&1
echo "===HEADER-count===" >> "$OUT"; git show HEAD:query-cosientist.md | grep -c '^## Iteration log' >> "$OUT" 2>&1
echo done