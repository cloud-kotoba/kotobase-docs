#!/bin/bash
# K-Z3 bench run166A-C (search) + landing control, same method as run165.
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench55_run166_out.txt
: > "$OUT"
date >> "$OUT"
uptime >> "$OUT"
for run in A B C; do
  echo "=== run166$run search ===" >> "$OUT"
  for i in $(seq 1 20); do
    ttfb=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' "https://search.kotobase.net/search?q=test")
    echo "166$run $i $ttfb" >> "$OUT"
  done
done
echo "=== landing control ===" >> "$OUT"
for i in $(seq 1 20); do
  ttfb=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' "https://kotobase.net/")
  echo "LC $i $ttfb" >> "$OUT"
done
date >> "$OUT"
