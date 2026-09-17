#!/bin/bash
# K-Z3 10時台 n積み増し run546 - same method: n=20 x 3 separate-conn curl + landing control
# format: "i code ttfb", single -w "%{http_code} %{time_starttransfer}"
B=$(date +%s)
DIR=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"

run_one () { # $1=label $2=url $3=outfile
  local lbl="$1" url="$2" out="$3"
  for i in $(seq 1 20); do
    res=$(curl -s -o /dev/null --max-time 25 -w "%{http_code} %{time_starttransfer}" "$url")
    echo "$i $res" >> "$out"
  done
}

run_one A "$SEARCH" "$DIR/.b532_run546A.ttfb" &
run_one B "$SEARCH" "$DIR/.b532_run546B.ttfb" &
run_one C "$SEARCH" "$DIR/.b532_run546C.ttfb" &
wait

run_one land "$LAND" "$DIR/.b532_run546land.ttfb"

E=$(date +%s)
echo "elapsed=$((E-B))s" > "$DIR/.b532_elapsed.txt"
date "+%Y-%m-%d %H:%M:%S %Z" > "$DIR/.b532_t0.txt"
uptime > "$DIR/.b532_uptime.txt"
echo done
