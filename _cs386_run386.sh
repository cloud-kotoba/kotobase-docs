#!/bin/sh
# cosientist core: K-Z3 18hr(9/7) n-add run384A-C, same method: n=20 x 3 + landing control,
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _cs384_time384.txt
run_search _cs384_384A.txt
run_search _cs384_384B.txt
run_search _cs384_384C.txt
run_land _cs384_land384.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _cs384_time384.txt
uptime >> _cs384_time384.txt
echo "done" >> _cs384_time384.txt