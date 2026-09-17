#!/bin/bash
# K-Z3 3時台 run530A-C measurement: 20 x 3 search + 20 landing control
# separate-conn curl, cold>=0.5s TTFB, single -w "%{http_code} %{time_starttransfer}"
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

run_one A "$SEARCH" "$DIR/.b530_A.ttfb" &
run_one B "$SEARCH" "$DIR/.b530_B.ttfb" &
run_one C "$SEARCH" "$DIR/.b530_C.ttfb" &
wait

run_one land "$LAND" "$DIR/.b530_landing.ttfb"

E=$(date +%s)
echo "elapsed=$((E-B))s" > "$DIR/.b530_elapsed.txt"
echo done