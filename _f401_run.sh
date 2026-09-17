#!/bin/sh
# falsify K-Z3 22hr n-add run401A-C, same method: n=20 x 3 + landing control,
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _f401_time.txt
run_search _f401_401A.txt
run_search _f401_401B.txt
run_search _f401_401C.txt
run_land _f401_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _f401_time.txt
uptime >> _f401_time.txt
echo "done" >> _f401_time.txt