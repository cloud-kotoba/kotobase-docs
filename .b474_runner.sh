#!/bin/bash
# K-Z3 14:00 hour n-add: run474A-C (n=20 each) + landing control, independent of sibling run473.
# falsify tick 2026-09-08 14:5x JST, separate-conn curl, cold>=0.5s TTFB. Matches run470/472 method.
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b474"
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
emit() { # $1=url $2=file
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' --connect-timeout 10 --max-time 30 "$1" >> "$2" 2>/dev/null
  done
}
t0=$(date '+%s.%N')
emit "$SEARCH" "${OUT}_A.raw"
emit "$SEARCH" "${OUT}_B.raw"
emit "$SEARCH" "${OUT}_C.raw"
emit "$LANDING" "${OUT}_landing.raw"
t1=$(date '+%s.%N')
echo "BIG474 elapsed_sec $t0 $t1" > "${OUT}_t0.txt"
echo done