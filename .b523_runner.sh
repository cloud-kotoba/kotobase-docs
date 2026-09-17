#!/bin/bash
# falsify 232 K-Z3 1hr band-first run523A-C + landing control
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
  run_series "search$s" "$SRCH" "$BASE/.b523_run523$s.ttfb"
done
run_series "landing" "$CTRL" "$BASE/.b523_landing.ttfb"
echo "all runs complete"