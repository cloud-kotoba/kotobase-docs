#!/bin/bash
# K-Z3 production HTTP measurement runner (falsify 第236回, run529). 3 x n=20 search + n=20 landing control.
# Separate curl connections, TTFB via time_starttransfer.
OUT="$1"
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
now() { date '+%s.%N'; }
t0=$(now)
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_A.ttfb" 2>/tmp/b529_curl_A.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_B.ttfb" 2>/tmp/b529_curl_B.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time  20 "$SEARCH" >> "${OUT}_C.ttfb" 2>/tmp/b529_curl_C.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 10 "$LANDING" >> "${OUT}_landing.ttfb" 2>/tmp/b529_curl_L.err
done
t1=$(now)
echo "run529 elapsed_sec $t0 $t1" > "${OUT}_t0.txt"
echo "consume $t1" > /dev/null