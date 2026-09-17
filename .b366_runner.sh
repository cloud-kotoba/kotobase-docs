#!/bin/sh
# bench K-Z3 15hr(9/7) n-add run366 (n=20 x 3 + landing control).
# true progressive NEXT from iter-log HEAD (bench 158, 15:12): next run ID run366.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b366_time.txt
uptime >> .b366_time.txt
run_url "$SEARCH" .b366_366A.txt
run_url "$SEARCH" .b366_366B.txt
run_url "$SEARCH" .b366_366C.txt
run_url "$LAND" .b366_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b366_time.txt
uptime >> .b366_time.txt