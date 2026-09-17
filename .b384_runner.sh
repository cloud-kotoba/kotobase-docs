#!/bin/sh
# falsify K-Z3 18hr(9/7) n-add run384.
# true NEXT from iter-log HEAD (bench 第169回): "委ねる; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し続行, 次 run ID は run384 使用".
# run384: independent 18hr measurement (run381=bench168, run382=falsify173, run383=bench169 committed/observed).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b384_time.txt
uptime >> .b384_time.txt
run_url "$SEARCH" .b384_384A.txt
run_url "$SEARCH" .b384_384B.txt
run_url "$SEARCH" .b384_384C.txt
run_url "$LAND" .b384_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b384_time.txt
uptime >> .b384_time.txt
echo "done rc=$?"