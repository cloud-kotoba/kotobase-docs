#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank_fetch.out
: > "$OUT"
echo "===REMOTE===" >> "$OUT"; git remote -v >> "$OUT" 2>&1
echo "===FETCH-net-kotobase===" >> "$OUT"; git fetch net-kotobase 2>&1 | head -20 >> "$OUT" 2>&1
echo "===FETCH-bench_fetch===" >> "$OUT"; git fetch bench_fetch 2>&1 | head -20 >> "$OUT" 2>&1
echo "===HEAD===" >> "$OUT"; git rev-parse HEAD >> "$OUT" 2>&1
echo "===rev-parse net-kotobase/main===" >> "$OUT"; git rev-parse net-kotobase/main >> "$OUT" 2>&1
echo "===rev-parse bench_fetch/main===" >> "$OUT"; git rev-parse bench_fetch/main >> "$OUT" 2>&1
echo done