#!/bin/bash
# cosientist run508 K-Z3 22h-band n-add measurement (ver 2: captures http_code + TTFB)
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
OUT=/tmp/cosient_run508v2
mkdir -p "$OUT"
echo "t0 $(date +%Y%m%d_%H%M%S)" > "$OUT/meta.txt"
uptime >> "$OUT/meta.txt"
for r in A B C; do
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" --max-time 30 "$SEARCH" >> "$OUT/run$r.raw"
  done
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" --max-time 30 "$LAND" >> "$OUT/land.raw"
done
echo "done $(date +%H:%M:%S)" >> "$OUT/meta.txt"
