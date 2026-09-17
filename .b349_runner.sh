#!/bin/sh
# cosientist K-Z3 12hr band n-add run349A-C (n=20 x 3 + landing control).
# same method: separate-connection curl, TTFB time_starttransfer, cold>=0.5s,
# nearest-rank p50. production HTTP, gate-exempt (host load1 >7.5).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b349_time.txt
uptime >> .b349_time.txt
run_url "$SEARCH" .b349_349A.txt
run_url "$SEARCH" .b349_349B.txt
run_url "$SEARCH" .b349_349C.txt
run_url "$LAND" .b349_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b349_time.txt
uptime >> .b349_time.txt