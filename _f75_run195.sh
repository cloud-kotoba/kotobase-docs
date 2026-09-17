#!/bin/bash
# falsify 75: K-Z3 8時台 1セット目 run195A-C (n=20 x3) + landing control
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/signup"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f75_run195_out.txt"
: > "$OUT"
for rid in 195A 195B 195C; do
  echo "=== run$rid search ===" >> "$OUT"
  for i in $(seq 1 20); do
    curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
  done
done
echo "=== landing control ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_L" >> "$OUT"
done
date '+%H:%M:%S JST' >> "$OUT"
uptime >> "$OUT"
echo done
