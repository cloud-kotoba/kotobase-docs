#!/bin/bash
# K-Z3 production HTTP measurement runner (bench run469, readjusted from 468 due to sibling in-flight).
# 3 x n=20 search + n=20 landing control. Separate curl connections, TTFB via time_starttransfer.
# Matches run467 method exactly.
OUT="$1"
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
now() { date '+%s.%N'; }
t0=$(now)
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_A.ttfb" 2>/dev/null
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_B.ttfb" 2>/dev/null
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_C.ttfb" 2>/dev/null
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$LANDING" >> "${OUT}_landing.ttfb" 2>/dev/null
done
t1=$(now)
echo "BIG470 elapsed_sec $t0 $t1" > "${OUT}_t0.txt"
echo "consume $t1" > /dev/null