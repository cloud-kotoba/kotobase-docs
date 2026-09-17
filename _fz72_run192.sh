#!/bin/bash
# K-Z3 07:00 hour first sample: run192A-C (n=20 each) + landing control
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_fz72_run192_out.txt"
: > "$OUT"
for rid in 192A 192B 192C; do
  echo "=== run$rid search ===" >> "$OUT"
  for i in $(seq 1 20); do
    curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
  done
done
echo "=== landing control ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_L" >> "$OUT"
done
echo done
