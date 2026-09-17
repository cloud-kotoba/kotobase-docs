#!/bin/sh
# bench K-Z3 16hr(9/7) band-first run368 (n=20 x 3 + landing control).
# true progressive NEXT from iter-log HEAD (rank 158, 15:46): K-Z3 16hr band-first run368.
# same method: separate-conn curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
run_url() {
  url="$1"; out="$2"; i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\\n" "$url" >> "$out"
    i=$((i+1))
  done
}
date '+start %Y-%m-%dT%H:%M:%S%z' > .b368_time.txt
uptime >> .b368_time.txt
run_url "$SEARCH" .b368_368A.txt
run_url "$SEARCH" .b368_368B.txt
run_url "$SEARCH" .b368_368C.txt
run_url "$LAND" .b368_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b368_time.txt
uptime >> .b368_time.txt