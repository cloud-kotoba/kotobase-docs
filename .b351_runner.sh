#!/bin/sh
# bench K-Z3 13hr(9/7) band-first run351A-C (n=20 x 3 + landing control).
# NEXT rank152: K-Z3 13時台帯初計測 run351. same method: separate-conn curl,
# TTFB time_starttransfer, cold>=0.5s, nearest-rank p50. production HTTP, gate-exempt.
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b351_time.txt
uptime >> .b351_time.txt
run_url "$SEARCH" .b351_351A.txt
run_url "$SEARCH" .b351_351B.txt
run_url "$SEARCH" .b351_351C.txt
run_url "$LAND" .b351_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b351_time.txt
uptime >> .b351_time.txt