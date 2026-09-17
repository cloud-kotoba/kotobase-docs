#!/bin/sh
# falsify K-Z3 current-band(10hr) n-add run335A-C, same method: n=20 x 3 +
# landing control, separate-connection curl, cold threshold >= 0.5s TTFB.
# production HTTP, gate-exempt.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _f156_time335.txt
run_search _f156_335A.txt
run_search _f156_335B.txt
run_search _f156_335C.txt
run_land _f156_land335.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _f156_time335.txt
uptime >> _f156_time335.txt
echo "done" >> _f156_time335.txt