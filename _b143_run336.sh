#!/bin/sh
# bench K-Z3 10hr n-add run336A-C, same method: n=20 x 3 + landing control,
# separate-connection curl, cold threshold >= 0.5s TTFB. production HTTP, gate-exempt.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _b143_time336.txt
run_search _b143_336A.txt
run_search _b143_336B.txt
run_search _b143_336C.txt
run_land _b143_land336.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _b143_time336.txt
uptime >> _b143_time336.txt
echo "done" >> _b143_time336.txt