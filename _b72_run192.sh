#!/bin/bash
# K-Z3 production HTTP measurement, same-method contract adapted to production:
# 3 sequential sets of n=20 (first-request-of-set = cold candidate), + landing control n=20.
# No secrets. Records only status codes and timings.
OUT=_b72_run192.txt
: > "$OUT"
EP="https://engine.kotobase.net/"
for s in A B C; do
  echo "SET $s" >> "$OUT"
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{http_code} %{time_total}\n" "$EP" >> "$OUT"
  done
done
echo "CONTROL landing /" >> "$OUT"
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_total}\n" "https://kotobase.net/" >> "$OUT"
done
date '+%H:%M:%S JST' >> "$OUT"
uptime >> "$OUT"
