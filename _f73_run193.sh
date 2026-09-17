#!/bin/bash
# falsify 73: K-Z3 7時台 n 積み増し run193A-C (n=20 x3) + landing control
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f73_run193_out.txt"
: > "$OUT"
for rid in 193A 193B 193C; do
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
