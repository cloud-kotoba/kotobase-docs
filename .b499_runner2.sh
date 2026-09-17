#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
UL="https://search.kotobase.net/search?q=test"
N=20
for idx in A B C; do
  out=".b499_run499${idx}.ttfb"
  : > "$out"
  for i in $(seq 1 $N); do
    code=$(curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}" "$UL")
    echo "$code" >> "$out"
  done
done
echo "DONE"