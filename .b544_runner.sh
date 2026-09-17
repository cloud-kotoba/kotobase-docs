#!/bin/bash
# K-Z3 9時台 n積み増し run544 - same method: n=20 x 3 separate-conn curl + landing control
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"
N=20
for idx in A B C; do
  out=".b544_run544${idx}.ttfb"
  : > "$out"
  for i in $(seq 1 $N); do
    code=$(curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}" "$SEARCH")
    echo "$code" >> "$out"
  done
done
: > .b544_landing.ttfb
for i in $(seq 1 $N); do
  code=$(curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}" "$CONTROL")
  echo "$code" >> .b544_landing.ttfb
done
echo "DONE"