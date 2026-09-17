#!/bin/sh
# falsify K-Z3 23hr(9/7) n-add run405 (n=20 x 3 + landing control).
# NEXT from iter-log HEAD (bench 第183回, run404): "K-Z3 現在時刻帯 23時台 n 積み増し続行、次 run ID は run405 使用".
# run405 free (.b405 absent). same method: separate-conn curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b405_time.txt
uptime >> .b405_time.txt
run_url "$SEARCH" .b405_405A.txt
run_url "$SEARCH" .b405_405B.txt
run_url "$SEARCH" .b405_405C.txt
run_url "$LAND" .b405_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b405_time.txt
uptime >> .b405_time.txt
echo "done rc=$?"