#!/bin/bash
# K-Z3 3hr(03時台) n-add run419 production HTTP TTFB measurement  — RUN2 (correct endpoint)
# method: per contract n=20 x3 runs + landing control(kotobase.net/signup); warmup 2 excluded per series; separate-conn curl
# metric: TTFB==curl time_starttransfer; cold>=0.5s TTFB; nearest-rank p50
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b419
mkdir -p "$OUT" 2>/dev/null || mkdir -p "$OUT"
series=$1
if [ -z "$series" ]; then exit 9; fi
if [ "$series" = "land" ]; then url="$LAND"; else url="$SEARCH"; fi
outf="$OUT/run419b_${series}.txt"
: > "$outf"
for i in $(seq 1 22); do
  row=$(curl -s -o /dev/null --max-time 15 \
      -w "%{http_code}|%{time_starttransfer}|%{time_total}" "$url" 2>/dev/null)
  echo "${i}|${row}" >> "$outf"
  sleep 0.2
done
echo "run419b ${series} done" >> "$OUT/run419b_summary.txt"