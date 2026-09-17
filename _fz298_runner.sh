#!/bin/sh
# falsify K-Z3 current-band(3hr/deep-night) independent n-add run298A-C,
# same method: n=20 x 3 + landing control, separate-connection curl,
# cold threshold >= 0.5s TTFB.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _fz298_time298.txt
run_search _fz298_298A.txt
run_search _fz298_298B.txt
run_search _fz298_298C.txt
run_land _fz298_land298.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _fz298_time298.txt
uptime >> _fz298_time298.txt
echo "done" >> _fz298_time298.txt