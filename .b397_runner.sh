#!/bin/sh
# bench K-Z3 21hr band-first run397 (n=20 x 3 + landing control), same method.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
echo "collision check:" > .b397_collision.txt
ls .b396* .b397* 2>/dev/null >> .b397_collision.txt
date '+start %Y-%m-%dT%H:%M:%S%z' > .b397_time.txt
uptime >> .b397_time.txt
run_url() {
  url="$1"; out="$2"; i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$url" >> "$out"
    i=$((i+1))
  done
}
run_url "$SEARCH" .b397_397A.txt
run_url "$SEARCH" .b397_397B.txt
run_url "$SEARCH" .b397_397C.txt
run_url "$LAND" .b397_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b397_time.txt
uptime >> .b397_time.txt
echo DONE >> .b397_time.txt