#!/bin/bash
# K-Z3 measurement runner -- bench run508 (2026-09-08 21時台 n 積み増し, 5th set)
# Same method: n=20 x 3 search (search.kotobase.net/search?q=test) + landing
# control (kotobase.net/signup, n=20), separate curl connection per request,
# capture "%{http_code} %{time_starttransfer}", cold = TTFB>=0.5s, nearest-rank p50.
set -u
BASE="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
RAW="$BASE/.run508_raw"
mkdir -p "$RAW/runA" "$RAW/runB" "$RAW/runC" "$RAW/control"
SEARCH="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"

echo "t0=$(date '+%H:%M:%S')" > "$RAW/times.txt"

for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" --max-time 30 "$SEARCH" >> "$RAW/runA/resp.txt"
done
echo "A done $(date '+%H:%M:%S')" >> "$RAW/times.txt"

for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" --max-time 30 "$SEARCH" >> "$RAW/runB/resp.txt"
done
echo "B done $(date '+%H:%M:%S')" >> "$RAW/times.txt"

for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" --max-time 30 "$SEARCH" >> "$RAW/runC/resp.txt"
done
echo "C done $(date '+%H:%M:%S')" >> "$RAW/times.txt"

for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" --max-time 30 "$CONTROL" >> "$RAW/control/resp.txt"
done
echo "control done $(date '+%H:%M:%S')" >> "$RAW/times.txt"
echo "MEASURE_COMPLETE" >> "$RAW/times.txt"