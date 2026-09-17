#!/bin/bash
# K-Z3 measurement runner -- bench run503 (2026-09-08 20時台 n-accum, 5th set)
# Method: n=20 x 3 search runs (search.kotobase.net/search?q=test) + landing control
# (kotobase.net/signup, n=20), separate curl connection per request,
# capture "%{http_code} %{time_starttransfer}", cold = TTFB>=0.5s, nearest-rank p50.
# Single -w (one -w only: code + ttfb), --max-time 30, no multi -w.
set -u
BASE="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
RAW="$BASE/.run503_raw"
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