#!/bin/sh
# bench K-Z3 19hr(9/7) n-add run391 (n=20 x 3 + landing control).
# NEXT from iter-log HEAD (bench 第173回, 19:41): "委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 19時台 n 積み増し続行、次 run ID は run391 使用".
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b391_time.txt
uptime >> .b391_time.txt
run_url "$SEARCH" .b391_391A.txt
run_url "$SEARCH" .b391_391B.txt
run_url "$SEARCH" .b391_391C.txt
run_url "$LAND" .b391_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b391_time.txt
uptime >> .b391_time.txt
echo "done rc=$?"