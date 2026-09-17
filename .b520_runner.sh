#!/bin/bash
# falsify 231 K-Z3 1hr band-first run520A-C + landing control
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
  run_series "search$s" "$SRCH" "$BASE/.b520_run520$s.ttfb"
done
run_series "landing" "$CTRL" "$BASE/.b520_landing.ttfb"
echo "all runs complete"