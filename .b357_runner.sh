#!/bin/sh
# bench 第154回 K-Z3 13hr(9/7) run357 n-add (n=20 x 3 + landing control), collision-relabel from run356.
# run356 already measured in-flight by cosientist 第124回 (.b356 files, 13:51).
# NEXT (bench 第153回 iter-log): K-Z3 current-band 13時台 n-add, run356 -> relabel run357.
# same method: separate-conn curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
run_url() {
  url="$1"; out="$2"; i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$url" >> "$out"
    i=$((i+1))
  done
}
date '+start %Y-%m-%dT%H:%M:%S%z' > .b357_time.txt
uptime >> .b357_time.txt
run_url "$SEARCH" .b357_357A.txt
run_url "$SEARCH" .b357_357B.txt
run_url "$SEARCH" .b357_357C.txt
run_url "$LAND" .b357_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b357_time.txt
uptime >> .b357_time.txt