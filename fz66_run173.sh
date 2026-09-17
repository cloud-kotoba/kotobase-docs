#!/bin/bash
# falsify 22時台 n 積み増し run173A-C (search) + landing control, same method as run172:
# n=20 per run, separate curl connections, TTFB per request.
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/fz66_run173_out.txt
: > "$OUT"
date >> "$OUT"
uptime >> "$OUT"
for run in A B C; do
  echo "=== run173$run search ===" >> "$OUT"
  for i in $(seq 1 20); do
    ttfb=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' "https://search.kotobase.net/search?q=test")
    echo "173$run $i $ttfb" >> "$OUT"
  done
done
echo "=== landing control ===" >> "$OUT"
for i in $(seq 1 20); do
  ttfb=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' "https://kotobase.net/")
  echo "LC $i $ttfb" >> "$OUT"
done
date >> "$OUT"
uptime >> "$OUT"
