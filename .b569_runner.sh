#!/bin/bash
# K-Z3 13時台 n 積み増し run569A-C (corrected endpoint search.kotobase.net, 同測定法) + landing control, falsify
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
date '+%F %T' > .b569_t0.txt
for S in A B C; do
  for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
    curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' -H 'Connection: close' 'https://search.kotobase.net/search?q=test' >> .b569_$S.ttfb
  done
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' -H 'Connection: close' 'https://kotobase.net/signup' >> .b569_ctl.ttfb
done
date '+%F %T' >> .b569_t0.txt
