#!/bin/sh
# falsify K-Z3 15hr(9/7) band-first n-add run365 (n=20 x 3 + landing control).
# relabel from run364 collision w/ bench158 in-flight (shared worktree .b364 double-append -> contaminated 40-line series discarded).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b365_time.txt
uptime >> .b365_time.txt
run_url "$SEARCH" .b365_365A.txt
run_url "$SEARCH" .b365_365B.txt
run_url "$SEARCH" .b365_365C.txt
run_url "$LAND" .b365_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b365_time.txt
uptime >> .b365_time.txt