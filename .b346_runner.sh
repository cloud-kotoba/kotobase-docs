#!/bin/sh
# bench K-Z3 12hr band n-add run346A-C (relabeled from run345: sibling falsify run345
# in-flight at 12:17-12:18, uncommitted). same method: n=20 x 3 + landing control,
# separate-connection curl, TTFB time_starttransfer, cold>=0.5s. production HTTP, gate-exempt.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
run_url() {
  url="$1"; out="$2"; i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$url" >> "$out"
    i=$((i+1))
  done
}
date '+start %Y-%m-%dT%H:%M:%S%z' > .b346_time.txt
uptime >> .b346_time.txt
run_url "$SEARCH" .b346_346A.txt
run_url "$SEARCH" .b346_346B.txt
run_url "$SEARCH" .b346_346C.txt
run_url "$LAND" .b346_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b346_time.txt
uptime >> .b346_time.txt