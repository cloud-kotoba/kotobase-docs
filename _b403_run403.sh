#!/bin/sh
# bench K-Z3 23hr(9/7) band-first run403A-C, same method: n=20 x 3 + landing control,
# separate-connection curl, cold threshold >= 0.5s TTFB, nearest-rank p50.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _b403_time403.txt
run_search _b403_403A.txt
run_search _b403_403B.txt
run_search _b403_403C.txt
run_land _b403_land403.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _b403_time403.txt
uptime >> _b403_time403.txt
echo "done" >> _b403_time403.txt