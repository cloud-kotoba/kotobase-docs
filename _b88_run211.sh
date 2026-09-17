#!/bin/sh
# bench 第87回 K-Z3 14時台 n 積み増し run211A-C + landing control
# 同一測定法: n=20 x 3 run, 別接続 curl, threshold cold >= 0.5s TTFB
set -e
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
run_search() {
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w '%{time_starttransfer}\n' "$SEARCH" >> "$1"
    i=$((i+1))
  done
}
run_land() {
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}\n' "$LAND" >> "$1"
    i=$((i+1))
  done
}
rm -f _b88_run211A.txt _b88_run211B.txt _b88_run211C.txt _b88_land.txt
run_search _b88_run211A.txt
run_search _b88_run211B.txt
run_search _b88_run211C.txt
run_land _b88_land.txt
date '+%H:%M:%S' >> _b88_time.txt
