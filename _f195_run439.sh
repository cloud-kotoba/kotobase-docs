#!/bin/sh
# falsify 第195回 K-Z3 8hr(9/8) set3 n-add run439A-C, same method: n=20 x 3 + landing control,
# separate-connection curl, cold threshold >= 0.5s TTFB. production HTTP, gate-exempt.
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
run_search() {
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$SEARCH" >> "$1"
    i=$((i+1))
  done
}
run_land() {
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$LAND" >> "$1"
    i=$((i+1))
  done
}
date '+start %Y-%m-%dT%H:%M:%S%z' > _f195_time439.txt
run_search _f195_439A.txt
run_search _f195_439B.txt
run_search _f195_439C.txt
run_land _f195_land439.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _f195_time439.txt
uptime >> _f195_time439.txt
echo "done" >> _f195_time439.txt