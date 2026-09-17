#!/bin/bash
# K-Z3 11hr band (falsify) run549A-C: 20 x 3 search + 20 landing control
# separate-conn curl, cold>=0.5s TTFB, TTFB-only per stats
OUT="$1"
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
now() { date '+%s.%N'; }
t0=$(now)
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_A.ttfb" 2>/tmp/b549_curl_A.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_B.ttfb" 2>/tmp/b549_curl_B.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_C.ttfb" 2>/tmp/b549_curl_C.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$LANDING" >> "${OUT}_landing.ttfb" 2>/tmp/b549_curl_L.err
done
t1=$(now)
echo "elapsed_sec $t0 $t1" > "${OUT}_t0.txt"
echo done
