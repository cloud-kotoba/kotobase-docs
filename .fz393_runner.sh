#!/bin/sh
# falsify: K-Z3 20時台 n-add run393A-C, same method: n=20 x 3 + landing control,
# separate-connection curl, TTFB capture, cold>=0.5s. production HTTP, gate-exempt.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
run_url() {
  url="$1"; out="$2"; i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$url" >> "$out"
    sleep 0.1
    i=$((i+1))
  done
}
date '+start %Y-%m-%dT%H:%M:%S%z' > .fz393_time.txt
run_url "$SEARCH" .fz393_393A.txt
run_url "$SEARCH" .fz393_393B.txt
run_url "$SEARCH" .fz393_393C.txt
run_url "$LAND" .fz393_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .fz393_time.txt
uptime >> .fz393_time.txt
echo "done" >> .fz393_time.txt