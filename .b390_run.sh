#!/bin/sh
# bench K-Z3 18hr(9/7) n-add run385 (n=20 x 3 + landing control).
# true NEXT from iter-log HEAD (rank 第163回): "K-Z3 18時台 n 積み増し継続 ... 次 run ID は run384 使用".
# run384 claimed by sibling falsify (.b384 data measured 18:44, in-flight commit) -> renumber to run385 (run216/run256/run263/run278 precedent, same-band independent measurement).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b385_time.txt
uptime >> .b385_time.txt
run_url "$SEARCH" .b385_385A.txt
run_url "$SEARCH" .b385_385B.txt
run_url "$SEARCH" .b385_385C.txt
run_url "$LAND" .b385_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b385_time.txt
uptime >> .b385_time.txt
echo "done rc=$?"