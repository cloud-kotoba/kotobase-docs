#!/bin/sh
# bench K-Z3 22hr band-first n-add run402A-C (run401 taken in-flight by falsify -> run402),
# same method: n=20 x 3 + landing control, separate-connection curl,
# cold threshold >= 0.5s TTFB. production HTTP, gate-exempt.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _b402_time.txt
run_search _b402_402A.txt
run_search _b402_402B.txt
run_search _b402_402C.txt
run_land _b402_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _b402_time.txt
uptime >> _b402_time.txt
echo "done" >> _b402_time.txt