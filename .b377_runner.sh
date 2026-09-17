#!/bin/sh
# bench K-Z3 17hr n-add run377 (n=20 x 3 + landing control), same method.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b377_time.txt
uptime >> .b377_time.txt
run_url "$SEARCH" .b377_377A.txt
run_url "$SEARCH" .b377_377B.txt
run_url "$SEARCH" .b377_377C.txt
run_url "$LAND" .b377_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b377_time.txt
uptime >> .b377_time.txt