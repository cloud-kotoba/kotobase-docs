#!/bin/sh
# falsify 121: K-Z3 23hr n-add run266A-C, same measurement method:
# n=20 x 3 runs + landing control, separate-connection curl, cold >= 0.5s TTFB.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
run_search() {
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "200 %{time_starttransfer}\n" "$SEARCH" >> "$1"
    i=$((i+1))
  done
}
run_land() {
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "200 %{time_starttransfer}\n" "$LAND" >> "$1"
    i=$((i+1))
  done
}
run_search _f121_run266A.txt
run_search _f121_run266B.txt
run_search _f121_run266C.txt
run_land _f121_land266.txt
date '+%Y-%m-%dT%H:%M:%S%z' > _f121_run266_time.txt
uptime >> _f121_run266_time.txt
echo "done" >> _f121_run266_time.txt