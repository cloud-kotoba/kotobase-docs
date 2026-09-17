#!/bin/bash
# bench 226 K-Z3 23hr n-add run512A-C + landing control 
BASE=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SRCH="https://search.kotobase.net/search?q=test"
CTRL="https://kotobase.net/signup"
FMT='%{http_code} %{time_starttransfer}'
run_series() {
  local name="$1"; local url="$2"; local out="$3"
  : > "$out"
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "$FMT" "$url" >> "$out"
    echo >> "$out"
  done
  echo "$name done -> $out"
}
for s in A B C; do
  run_series "search$s" "$SRCH" "$BASE/.b512_run512$s.ttfb"
done
run_series "landing" "$CTRL" "$BASE/.b512_landing.ttfb"
echo "all runs complete"