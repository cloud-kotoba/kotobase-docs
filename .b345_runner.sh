#!/bin/sh
# falsify K-Z3 12hr band n-add run345A-C, same method: n=20 x 3 + landing control,
# separate-connection curl, cold threshold >= 0.5s TTFB. production HTTP, gate-exempt.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b345_time.txt
uptime >> .b345_time.txt
run_url "$SEARCH" .b345_345A.txt
run_url "$SEARCH" .b345_345B.txt
run_url "$SEARCH" .b345_345C.txt
run_url "$LAND" .b345_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b345_time.txt
uptime >> .b345_time.txt