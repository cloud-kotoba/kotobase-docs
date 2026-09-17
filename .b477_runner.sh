#!/bin/bash
# K-Z3 15時台 n 積み増し run477 (bench) — production HTTP, gate-exempt
# Method: n=20 x3 search + landing control, separate curl conns, TTFB (time_starttransfer), cold>=0.5s
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> .b477_A.ttfb 2>/dev/null
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> .b477_B.ttfb 2>/dev/null
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> .b477_C.ttfb 2>/dev/null
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$LANDING" >> .b477_landing.ttfb 2>/dev/null
done
echo "done"
wc -l .b477_A.ttfb .b477_B.ttfb .b477_C.ttfb .b477_landing.ttfb
