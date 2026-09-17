#!/bin/bash
# landing control: kotobase.net/signup, separate conn curl
LAND="https://kotobase.net/signup"
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b419
mkdir -p "$OUT" 2>/dev/null; mkdir -p "$OUT"
outf="$OUT/run419_land.txt"
: > "$outf"
for i in $(seq 1 22); do
  row=$(curl -s -o /dev/null --max-time 15 \
      -w "%{http_code}|%{time_starttransfer}|%{time_total}" "$LAND" 2>/dev/null)
  echo "${i}|${row}" >> "$outf"
  sleep 0.2
done
echo "run419 land done" >> "$OUT/run419_summary.txt"