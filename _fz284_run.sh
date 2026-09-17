#!/bin/sh
# falsify K-Z3 2時台(深夜帯) n-add run284A-C, same measurement method:
# n=20 x 3 search runs + landing control, separate-connection curl,
# cold threshold >= 0.5s TTFB (time_starttransfer).
# cron runtime restrictions: no -e/-c flags, no heredoc-to-interpreter, no rm -rf.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _fz284_time.txt
run_search _fz284A.txt
run_search _fz284B.txt
run_search _fz284C.txt
run_land _fz284_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _fz284_time.txt
uptime >> _fz284_time.txt
echo "done" >> _fz284_time.txt