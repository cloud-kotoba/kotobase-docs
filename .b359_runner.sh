#!/bin/sh
# bench K-Z3 14hr(9/7) band-first run359 (n=20 x 3 + landing control).
# NEXT (rank 第155回 iter-log, 14:03): K-Z3 14時台帯初計測, run359.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b359_time.txt
uptime >> .b359_time.txt
run_url "$SEARCH" .b359_359A.txt
run_url "$SEARCH" .b359_359B.txt
run_url "$SEARCH" .b359_359C.txt
run_url "$LAND" .b359_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b359_time.txt
uptime >> .b359_time.txt