#!/bin/sh
# falsify K-Z3 14hr(9/7) n-add run362 (n=20 x 3 + landing control).
# NEXT (falsify 第165回 iter-log, 14:34): 委ねる -> fallback K-Z3 現時刻帯 14時台 n積み増し続行, run362.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b362_time.txt
uptime >> .b362_time.txt
run_url "$SEARCH" .b362_362A.txt
run_url "$SEARCH" .b362_362B.txt
run_url "$SEARCH" .b362_362C.txt
run_url "$LAND" .b362_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b362_time.txt
uptime >> .b362_time.txt