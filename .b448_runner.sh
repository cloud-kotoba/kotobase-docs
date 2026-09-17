#!/bin/bash
# K-Z3 run448 measurement: 3 sets n=20 search + landing control n=20 signup
# Same method: curl separate connection, cold>=0.5s TTFB, nearest-rank p50
set -u
T0=$(date +%s%N)
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for s in A B C; do
  rm -f "$OUT/.b448_run448${s}.ttfb"
  for i in $(seq 1 20); do
    curl -sS -o /dev/null \
      -w "%{time_starttransfer}\n" \
      "https://search.kotobase.net/search?q=test" >> "$OUT/.b448_run448${s}.ttfb" 2>/dev/null
  done
done
# landing control
rm -f "$OUT/.b448_landing.ttfb"
for i in $(seq 1 20); do
  curl -sS -o /dev/null \
    -w "%{time_starttransfer}\n" \
    "https://kotobase.net/signup" >> "$OUT/.b448_landing.ttfb" 2>/dev/null
done
T1=$(date +%s%N)
echo "elapsed_ms=$(( (T1-T0)/1000000 ))" > "$OUT/.b448_elapsed.txt"
echo done