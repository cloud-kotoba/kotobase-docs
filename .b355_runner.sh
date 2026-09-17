#!/bin/sh
# bench K-Z3 13hr(9/7) run355 n-add (n=20 x 3 + landing control), bench 第153回.
# NEXT falsify163: K-Z3 current-band 13時台 n-add, run355. same method: separate-conn
# curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50. production HTTP, gate-exempt.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b355_time.txt
uptime >> .b355_time.txt
run_url "$SEARCH" .b355_355A.txt
run_url "$SEARCH" .b355_355B.txt
run_url "$SEARCH" .b355_355C.txt
run_url "$LAND" .b355_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b355_time.txt
uptime >> .b355_time.txt