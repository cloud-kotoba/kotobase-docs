#!/bin/bash
# bench 第231回 K-Z3 2時台 n-add run523A-C
# 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50
# 正 endpoint search.kotobase.net/search?q=test; control kotobase.net/signup
# 単一 -w で http_code + time_starttransfer を出力 (複数 -w は最後のみ有効のため)
SEARCH="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"
OUT=/tmp/run523_raw.txt
: > "$OUT"

for run in A B C; do
  for i in $(seq 1 20); do
    code_ttfb=$(curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}" --max-time 30 "$SEARCH")
    echo "SEARCH_${run}_${i} $code_ttfb" >> "$OUT"
    sleep 0.1
  done
done

# landing control n=20
for i in $(seq 1 20); do
  code_ttfb=$(curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}" --max-time 30 "$CONTROL")
  echo "CTRL_${i} $code_ttfb" >> "$OUT"
  sleep 0.1
done

echo "DONE" >> "$OUT"
echo "finished"
