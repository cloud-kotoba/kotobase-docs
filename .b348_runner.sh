#!/bin/sh
# bench K-Z3 12hr band n-add run348A-C.
# run-ID collision: sibling ran run347 in-flight at 12:36-12:37 (this tick),
# relabeled to run348 per precedent (run216/run256/run263). same method:
# n=20 x 3 + landing control, separate-connection curl, TTFB time_starttransfer,
# cold>=0.5s. production HTTP, gate-exempt (host load1 43.38).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b348_time.txt
uptime >> .b348_time.txt
run_url "$SEARCH" .b348_348A.txt
run_url "$SEARCH" .b348_348B.txt
run_url "$SEARCH" .b348_348C.txt
run_url "$LAND" .b348_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b348_time.txt
uptime >> .b348_time.txt