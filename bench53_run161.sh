#!/bin/bash
# K-Z3 bench run161A-C (search) + landing control, same method as prior runs:
# n=20 per run, separate curl connections, record TTFB per request.
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench53_run161_out.txt
: > "$OUT"
date >> "$OUT"
for run in A B C; do
  echo "=== run161$run search ===" >> "$OUT"
  for i in $(seq 1 20); do
    ttfb=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' "https://search.kotobase.net/search?q=test")
    echo "161$run $i $ttfb" >> "$OUT"
  done
done
echo "=== landing control ===" >> "$OUT"
for i in $(seq 1 20); do
  ttfb=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' "https://kotobase.net/")
  echo "LC $i $ttfb" >> "$OUT"
done
date >> "$OUT"
