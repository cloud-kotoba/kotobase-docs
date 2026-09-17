#!/bin/sh
# bench K-Z3 4hr(deep-night) n-add run305A-C, same method: n=20 x 3 + landing control,
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
date '+start %Y-%m-%dT%H:%M:%S%z' > _b305_time305.txt
run_search _b305_305A.txt
run_search _b305_305B.txt
run_search _b305_305C.txt
run_land _b305_land305.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> _b305_time305.txt
uptime >> _b305_time305.txt
echo "done" >> _b305_time305.txt