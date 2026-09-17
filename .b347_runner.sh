#!/bin/sh
# falsify K-Z3 12hr band n-add run347A-C, same method n=20 x 3 + landing control
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b347_time.txt
uptime >> .b347_time.txt
run_url "$SEARCH" .b347_347A.txt
run_url "$SEARCH" .b347_347B.txt
run_url "$SEARCH" .b347_347C.txt
run_url "$LAND" .b347_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b347_time.txt
uptime >> .b347_time.txt