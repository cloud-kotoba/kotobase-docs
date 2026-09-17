#!/bin/bash
# K-Z3 20時台 n Add run500 - same method: n=20 x 3 separate-conn curl + landing control
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"
N=20
UL="https://search.kotobase.net/search?q=test"
for idx in A B C; do
  out=".b500_run500${idx}.ttfb"
  : > "$out"
  for i in $(seq 1 $N); do
    code=$(curl -s -o /dev/null -w "%{http_code}" -w " %{time_starttransfer}" "$UL")
    echo "$code" >> "$out"
  done
done
: > .b500_landing.ttfb
for i in $(seq 1 $N); do
  code=$(curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}" "$CONTROL")
  echo "$code" >> .b500_landing.ttfb
done
echo "DONE"