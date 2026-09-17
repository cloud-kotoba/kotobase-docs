#!/bin/sh
# falsify K-Z3 7hr(9/8) run434 n-add (n=20 x 3 + landing control), falsify 第192回.
# NEXT rank190: K-Z3 7hr(7時台) n-add run434. same method: separate-conn
# curl, TTFB time_starttransfer), cold>=0.5s, nearest-rank p50. production HTTP, gate-exempt.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .f192_run434_time.txt
uptime >> .f192_run434_time.txt
run_url "$SEARCH" .f192_run434_434A.txt
run_url "$SEARCH" .f192_run434_434B.txt
run_url "$SEARCH" .f192_run434_434C.txt
run_url "$LAND" .f192_run434_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .f192_run434_time.txt
uptime >> .f192_run434_time.txt