#!/bin/sh
# falsify K-Z3 24hr(0hr) n-add run271A-C, same measurement method: n=20 x 3 runs + landing control,
# separate-connection curl, cold threshold >= 0.5s TTFB.
# cron runtime restrictions: no -e/-c flags, no heredoc-to-interpreter, no rm -rf.
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
run_search _f124_run271A.txt
run_search _f124_run271B.txt
run_search _f124_run271C.txt
run_land _f124_land271.txt
date '+%Y-%m-%dT%H:%M:%S%z' > _f124_run271_time.txt
uptime >> _f124_run271_time.txt
echo "done" >> _f124_run271_time.txt