#!/bin/sh
# falsify K-Z3 19hr(9/7) n-add run390 (n=20 x 3 + landing control).
# true NEXT from iter-log HEAD (rank 第165回): "委ねる (rank 指定優先;フォールバックは K-Z3 現在時刻帯 19時台 n 積み増し続行, 次 run ID は run390 使用".
# 19hr 4-set: bench run387(6/60)+falsify run388(3/60)+bench run389(4/60)=13/180 ~7.2% 済みの積み増し続行.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b390_time.txt
uptime >> .b390_time.txt
run_url "$SEARCH" .b390_390A.txt
run_url "$SEARCH" .b390_390B.txt
run_url "$SEARCH" .b390_390C.txt
run_url "$LAND" .b390_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b390_time.txt
uptime >> .b390_time.txt
echo "done rc=$?"