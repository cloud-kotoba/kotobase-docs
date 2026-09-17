#!/bin/bash
# K-Z3 midnight band (00:00 hour): run102A-C (n=20 each) + landing control
# claim contract: same method as run98-101 (separate-connection curl, Tokyo)
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run102_out.txt"
: > "$OUT"
echo "start $(date)" >> "$OUT"
for rid in 102A 102B 102C; do
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
echo done
