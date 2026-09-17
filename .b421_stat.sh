#!/bin/bash
# stat helper per file: n, ok200-count, cold(>=0.5s) count+values, p50(sorted 10th for n=20), min, max
set -u
CD="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
cd "$CD"
out="$CD/.b421_stats_out.txt"
: > "$out"
for f in .b421_run421_A.txt .b421_run421_B.txt .b421_run421_C.txt .b421_run421_land.txt; do
  echo "=== $f ===" >> "$out"
  n=$(wc -l < "$f")
  ok=$(awk '{if ($1=="200") c++} END{print c+0}' "$f")
  echo "n=$n ok200=$ok" >> "$out"
  echo "cold_count=$(awk '{if ($2>=0.5) c++} END{print c+0}' "$f")" >> "$out"
  echo "cold_values:$(awk '{if ($2>=0.5) printf " %.3f", $2} END{print ""}' "$f")" >> "$out"
  echo "p50=$(sort -k2 -n "$f" | sed -n '10p' | awk '{print $2}')" >> "$out"
  echo "min=$(sort -k2 -n "$f" | sed -n '1p' | awk '{print $2}')" >> "$out"
  echo "max=$(sort -k2 -rn "$f" | sed -n '1p' | awk '{print $2}')" >> "$out"
done
echo "stat done" >> "$out"