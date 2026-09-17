#!/bin/bash
# K-Z3 14:00 hour n-add: run472A-C (n=20 each) + landing control
# bench tick 2026-09-08 14:2x JST, separate-conn curl, cold>=0.5s TTFB
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/signup"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b472_out.txt"
: > "$OUT"
for rid in 472A 472B 472C; do
  echo "=== run$rid search ===" >> "$OUT"
  for i in $(seq 1 20); do
    curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" --max-time 30 "$URL_S" >> "$OUT"
  done
done
echo "=== landing control ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" --max-time 30 "$URL_L" >> "$OUT"
done
echo done >> "$OUT"
echo "MEASURE_DONE rc=$?"