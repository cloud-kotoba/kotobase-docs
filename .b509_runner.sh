#!/bin/bash
# K-Z3 22hr n-add run509A-C + landing control
# same method: n=20 x 3 search + landing control, separate-conn curl,
# cold>=0.5s TTFB, single -w "%{http_code} %{time_starttransfer}"
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
  run_series "search$s" "$SRCH" "$BASE/.b509_run509$s.ttfb"
done
run_series "landing" "$CTRL" "$BASE/.b509_landing.ttfb"
echo "all runs complete"