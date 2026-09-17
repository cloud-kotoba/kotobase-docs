#!/bin/sh
# bench K-Z3 19hr(9/7) band-first run386 (n=20 x 3 + landing control).
# true NEXT from iter-log HEAD (rank 第163回): "実行時刻が 18時台内なら積み増し続行, 19時台移行後は 19時台帯初計測へ".
# current tick 19:05 JST -> 19時台带初計測, run ID 386 (run384/385 used by siblings, .b386 not present = no collision).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b386_time.txt
uptime >> .b386_time.txt
run_url "$SEARCH" .b386_386A.txt
run_url "$SEARCH" .b386_386B.txt
run_url "$SEARCH" .b386_386C.txt
run_url "$LAND" .b386_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b386_time.txt
uptime >> .b386_time.txt
echo "done rc=$?"