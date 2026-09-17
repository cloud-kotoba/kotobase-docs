#!/bin/bash
# bench 第92回: K-Z3 現在時刻帯 16時台 n 積み増し run224A-C (n=20 x3) + landing control
# 同測定法: search.kotobase.net/search?q=test, 別接続 curl, cold >= 0.5s TTFB
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_b92_run224_out.txt"
: > "$OUT"
echo "start $(date)" >> "$OUT"
for rid in 224A 224B 224C; do
  echo "=== run$rid search ===" >> "$OUT"
  for i in $(seq 1 20); do
    curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
  done
done
echo "=== landing control ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_L" >> "$OUT"
done
echo "end $(date)" >> "$OUT"
uptime >> "$OUT"
echo done