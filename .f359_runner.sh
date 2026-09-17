#!/bin/sh
# falsify K-Z3 14hr band-first n-add run359A-C, same method: n=20 x 3 + landing control,
# separate-connection curl, cold threshold >= 0.5s TTFB. production HTTP, gate-exempt.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
run_url() {
  url="$1"; out="$2"; i=1
  while [ "$i" -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$url" >> "$out"
    i=$((i+1))
  done
}
date '+start %Y-%m-%dT%H:%M:%S%z' > .f359_time.txt
run_url "$SEARCH" .f359_359A.txt
run_url "$SEARCH" .f359_359B.txt
run_url "$SEARCH" .f359_359C.txt
run_url "$LAND" .f359_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .f359_time.txt
uptime >> .f359_time.txt
echo "done" >> .f359_time.txt