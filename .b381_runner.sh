#!/bin/sh
# bench K-Z3 18hr(9/7) n-add run381 (n=20 x 3 + landing control).
# true NEXT from iter-log HEAD: cosientist 第126回 "次 run ID は run381 使用".
# run381: independent 18hr measurement (run380 was consumed by committed 17hr run + falsify in-flight).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b381_time.txt
uptime >> .b381_time.txt
run_url "$SEARCH" .b381_381A.txt
run_url "$SEARCH" .b381_381B.txt
run_url "$SEARCH" .b381_381C.txt
run_url "$LAND" .b381_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b381_time.txt
uptime >> .b381_time.txt
echo "done rc=$?"