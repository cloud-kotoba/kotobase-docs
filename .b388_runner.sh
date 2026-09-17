#!/bin/sh
# falsify K-Z3 19hr(9/7) n-add run388 (n=20 x 3 + landing control).
# run388 = next run ID after bench 第171回 run387 (19:06, 19時台帯初計測, uncommitted in-flight).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b388_time.txt
uptime >> .b388_time.txt
run_url "$SEARCH" .b388_388A.txt
run_url "$SEARCH" .b388_388B.txt
run_url "$SEARCH" .b388_388C.txt
run_url "$LAND" .b388_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b388_time.txt
uptime >> .b388_time.txt
echo "done rc=$?"