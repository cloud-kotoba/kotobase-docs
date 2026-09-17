#!/bin/bash
# falsify 259th: K-Z3 23hr band-first (9/9) run574A-C, n=20 x3 + landing control
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
date '+%Y-%m-%d %H:%M:%S' > .fz259_t0.txt
for S in A B C; do
  : > .fz259_run574${S}.ttfb
  for i in $(seq 1 20); do
    code=$(curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}' --max-time 15 'https://search.kotobase.net/search?q=test')
    echo "$code" >> .fz259_run574${S}.ttfb
  done
done
: > .fz259_landing.ttfb
for i in $(seq 1 20); do
  code=$(curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}' --max-time 15 'https://kotobase.net/signup')
  echo "$code" >> .fz259_landing.ttfb
done
date '+%Y-%m-%d %H:%M:%S' >> .fz259_t0.txt
uptime >> .fz259_t0.txt
