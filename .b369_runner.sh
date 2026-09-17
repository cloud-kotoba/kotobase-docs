#!/bin/sh
# falsify K-Z3 16hr(9/7) n-add run369 (n=20 x 3 + landing control).
# second set after bench 第160回 run368 (band-first, cold 9/60 heavy 8/20).
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
date '+start %Y-%m-%dT%H:%M:%S%z' > .b369_time.txt
uptime >> .b369_time.txt
run_url "$SEARCH" .b369_369A.txt
run_url "$SEARCH" .b369_369B.txt
run_url "$SEARCH" .b369_369C.txt
run_url "$LAND" .b369_land.txt
date '+end %Y-%m-%dT%H:%M:%S%z' >> .b369_time.txt
uptime >> .b369_time.txt