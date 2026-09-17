#!/bin/sh
# cosientist K-Z3 0hr(9/8) n-add run407 (n=20 x 3 + landing control).
# NEXT from iter-log HEAD (bench 第184回, run406): "K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run407 使用".
# run407 free (.b407 absent). same method: separate-conn curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b407_time.txt
uptime >> .b407_time.txt
run_url "$SEARCH" .b407_407A.txt
run_url "$SEARCH" .b407_407B.txt
run_url "$SEARCH" .b407_407C.txt
run_url "$LAND" .b407_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b407_time.txt
uptime >> .b407_time.txt
echo "done rc=$?"