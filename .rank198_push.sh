#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank198_push.out
: > "$OUT"
echo "===PUSH-bench===" >> "$OUT"; git push bench_fetch HEAD:main >> "$OUT" 2>&1
echo "===PUSH-net===" >> "$OUT"; git push net-kotobase HEAD:main >> "$OUT" 2>&1
echo "===VERIFY-FETCH-bench===" >> "$OUT"; git fetch bench_fetch 2>&1 | head -3 >> "$OUT"
echo "===VERIFY-FETCH-net===" >> "$OUT"; git fetch net-kotobase 2>&1 | head -3 >> "$OUT"
echo "===HEAD===" >> "$OUT"; git rev-parse HEAD >> "$OUT" 2>&1
echo "===bench-main===" >> "$OUT"; git rev-parse bench_fetch/main >> "$OUT" 2>&1
echo "===net-main===" >> "$OUT"; git rev-parse net-kotobase/main >> "$OUT" 2>&1
echo done