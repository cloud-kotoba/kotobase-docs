#!/bin/bash
# K-Z3 8時台 n-add run444 tail completion (C 10-20 + landing 1-20)
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
export PATH="/usr/bin:/bin:/usr/sbin:/sbin"
OUT=.b197_run444
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
for i in $(seq 10 20); do
  t=$(curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}" --max-time 30 "$SEARCH" 2>/dev/null)
  echo "$i $t" >> "$OUT"_C.txt
done
for i in $(seq 1 20); do
  t=$(curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}" --max-time 30 "$LANDING" 2>/dev/null)
  echo "$i $t" >> "$OUT"_landing.txt
done
echo done