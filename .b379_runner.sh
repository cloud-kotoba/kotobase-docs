#!/bin/bash
# K-Z3 17時台 run379A-C n-add + landing control (cold>=0.5s, nearest-rank p50)
# same method n=20 x 3 + landing control, separate curl conn, cold>=0.5s threshold
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b379_
for run in A B C; do
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{time_total}\n" "$SEARCH" >> "${OUT}${run}.txt"
  done
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{time_total}\n" "$LAND" >> "${OUT}land.txt"
done
echo "done run379 $(date +%H:%M:%S)"