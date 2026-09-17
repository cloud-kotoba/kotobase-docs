#!/bin/sh
# falsify K-Z3 16hr(9/7) n-add run373A-C (next run ID per bench163/falsify170 iter-log).
# same method: n=20 x 3 + landing control, separate-connection curl, time_starttransfer, cold>=0.5s, production HTTP gate-exempt.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b373_time.txt
uptime >> .b373_time.txt
run_url "$SEARCH" .b373_373A.txt
run_url "$SEARCH" .b373_373B.txt
run_url "$SEARCH" .b373_373C.txt
run_url "$LAND" .b373_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b373_time.txt
uptime >> .b373_time.txt