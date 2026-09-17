#!/bin/bash
# K-Z3 production HTTP measurement run192A-C (retry with real endpoint):
# 3 sequential sets of n=20 on https://kotobase.net/ + landing control already measured (n=20, 07:10 JST, p50 225ms).
OUT=_b72_run192b.txt
: > "$OUT"
for s in A B C; do
  echo "SET $s" >> "$OUT"
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{http_code} %{time_total}\n" "https://kotobase.net/" >> "$OUT"
  done
done
date '+%H:%M:%S JST' >> "$OUT"
