#!/bin/sh
# bench K-Z3 16hr(9/7) n-add run370 (n=20 x 3 + landing control) 第161回.
# third set after bench run368 (band-first 9/60) + falsify run369 (collision, 2nd set).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b370_time.txt
uptime >> .b370_time.txt
run_url "$SEARCH" .b370_370A.txt
run_url "$SEARCH" .b370_370B.txt
run_url "$SEARCH" .b370_370C.txt
run_url "$LAND" .b370_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b370_time.txt
uptime >> .b370_time.txt