#!/bin/sh
# falsify K-Z3 15hr(9/7) n-add run367 (n=20 x 3 + landing control).
# true progressive NEXT from iter-log HEAD (bench 159,  ̃15:26): next run ID run367.
# same method: separate-conn curl, TTFB time_starttransfer, ̃cold>=0.5s, nearest-rank p50.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b367_time.txt
uptime >> .b367_time.txt
run_url "$SEARCH" .b367_367A.txt
run_url "$SEARCH" .b367_367B.txt
run_url "$SEARCH" .b367_367C.txt
run_url "$LAND" .b367_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b367_time.txt
uptime >> .b367_time.txt