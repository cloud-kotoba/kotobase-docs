#!/bin/sh
# bench K-Z3 18hr(9/7) n-add run383.
# true NEXT from iter-log HEAD (falsify 第173回): "K-Z3 現在時刻帯 18時台 n 積み増し続行, 次 run ID は run383 使用".
# run383: independent 18hr measurement (run382 = falsify173 committed).
# same method: separate-conn curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b420_time.txt
uptime >> .b420_time.txt
run_url "$SEARCH" .b420_run420_420A.txt
run_url "$SEARCH" .b420_run420_420B.txt
run_url "$SEARCH" .b420_run420_420C.txt
run_url "$LAND" .b420_run420_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b420_time.txt
uptime >> .b420_time.txt
echo "done rc=$?"