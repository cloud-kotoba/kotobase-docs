#!/bin/bash
# K-Z3 1時台(深夜帯) run521 n-add falsify tick. 3 x n=20 search + n=20 landing control.
# Separate curl connections, TTFB via time_starttransfer. cold threshold >=0.5s.
OUT="$1"
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_A.ttfb" 2>/tmp/fz521_curl_A.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_B.ttfb" 2>/tmp/fz521_curl_B.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$SEARCH" >> "${OUT}_C.ttfb" 2>/tmp/fz521_curl_C.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 --max-time 20 "$LANDING" >> "${OUT}_landing.ttfb" 2>/tmp/fz521_curl_L.err
done
echo done