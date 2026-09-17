#!/bin/sh
# falsify K-Z3 0hr(9/8) n-add run409 (n=20 x 3 + landing control).
# NEXT from iter-log HEAD (rank 第174回, f650bf8): "K-Z3 0hr n-add run409 + iter-log".
# run409 free (.b409 absent). same method: separate-conn curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b409_time.txt
uptime >> .b409_time.txt
run_url "$SEARCH" .b409_409A.txt
run_url "$SEARCH" .b409_409B.txt
run_url "$SEARCH" .b409_409C.txt
run_url "$LAND" .b409_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b409_time.txt
uptime >> .b409_time.txt
echo "done rc=$?"