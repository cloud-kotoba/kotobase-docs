#!/bin/bash
# cosientist run508 K-Z3 22h-band n-add measurement
# endpoint search.kotobase.net/search?q=test, n=20 x 3 + landing control (kotobase.net/signup n=20)
# cold >= 0.5s, nearest-rank p50
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
OUT=/tmp/cosient_run508
mkdir -p "$OUT"
TS=$(date +%Y%m%d_%H%M%S)
echo "t0 $TS" > "$OUT/meta.txt"
echo "hostload:" >> "$OUT/meta.txt"
uptime >> "$OUT/meta.txt"

for r in A B C; do
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{time_starttransfer}\n" --max-time 30 "$SEARCH" >> "$OUT/run$r.raw"
  done
done
# landing control
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{time_starttransfer}\n" --max-time 30 "$LAND" >> "$OUT/land.raw"
done
echo "done $(date +%H:%M:%S)" >> "$OUT/meta.txt"
