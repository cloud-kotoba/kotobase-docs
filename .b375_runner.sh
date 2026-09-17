#!/bin/sh
# cosientist K-Z3 17hr(9/7) band-first n-add run375 (n=20 x 3 + landing control).
# Same method: separate-conn curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b375_time.txt
uptime >> .b375_time.txt
run_url "$SEARCH" .b375_375A.txt
run_url "$SEARCH" .b375_375B.txt
run_url "$SEARCH" .b375_375C.txt
run_url "$LAND" .b375_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b375_time.txt
uptime >> .b375_time.txt