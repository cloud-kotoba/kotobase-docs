#!/bin/sh
# falsify K-Z3 18hr(9/7) n-add run380 (n=20 x 3 + landing control).
# true progressive NEXT from iter-log HEAD: K-Z3 current-band(18hr) n 積み増し継続, next run ID run380.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b380_time.txt
uptime >> .b380_time.txt
run_url "$SEARCH" .b380_380A.txt
run_url "$SEARCH" .b380_380B.txt
run_url "$SEARCH" .b380_380C.txt
run_url "$LAND" .b380_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b380_time.txt
uptime >> .b380_time.txt