#!/bin/sh
# cosientist K-Z3 3hr(deep-night) n-add run297A-C, same method: n=20 x 3 + landing control,
# separate-connection curl, cold threshold >= 0.5s TTFB.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _c297_time297.txt
run_search _c297_297A.txt
run_search _c297_297B.txt
run_search _c297_297C.txt
run_land _c297_land297.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _c297_time297.txt
uptime >> _c297_time297.txt
echo "done" >> _c297_time297.txt