#!/bin/sh
# bench 158 K-Z3 15hr band-first n-add run364A-C (n=20 x 3 + landing control).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b364_time.txt
uptime >> .b364_time.txt
run_url "$SEARCH" .b364_364A.txt
run_url "$SEARCH" .b364_364B.txt
run_url "$SEARCH" .b364_364C.txt
run_url "$LAND" .b364_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b364_time.txt
uptime >> .b364_time.txt