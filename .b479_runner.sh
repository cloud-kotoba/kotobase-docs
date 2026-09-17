#!/bin/bash
# K-Z3 16:00 hour band-first: run479A-C (n=20 each) + landing control.
# bench tick 2026-09-08 16:0x JST, separate-conn curl, cold>=0.5s TTFB. Matches run478 method.
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b479"
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
echo "BIG479 elapsed_sec $t0 $t1" > "${OUT}_t0.txt"
echo done