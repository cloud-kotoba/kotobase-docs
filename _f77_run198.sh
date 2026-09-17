#!/bin/sh
# falsify 第77回: K-Z3 8時台 n 積み増し run198A-C (n=20 x 3 + landing control, 別接続 curl)
OUT=_f77_run198_out.txt
: > "$OUT"
date "+%Y-%m-%d %H:%M:%S JST start" >> "$OUT"
for run in A B C; do
  echo "== run198$run ==" >> "$OUT"
  curl -s -o /dev/null -w "%{http_code} %{time_total} landing\n" "https://kotobase.net/" >> "$OUT"
  i=0
  while [ $i -lt 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_total}\n" "https://kotobase.net/search?q=$(date +%s%N)" >> "$OUT"
    i=$((i+1))
  done
  sleep 2
done
echo "== control (landing x20, 別接続) ==" >> "$OUT"
i=0
while [ $i -lt 20 ]; do
  curl -s -o /dev/null -w "%{http_code} %{time_total}\n" "https://kotobase.net/signup" >> "$OUT"
  i=$((i+1))
done
date "+%Y-%m-%d %H:%M:%S JST end" >> "$OUT"
