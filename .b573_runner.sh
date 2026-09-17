#!/bin/bash
# falsify: K-Z3 11時台 n 積み増し run573A-C (同測定法, search.kotobase.net/search?q=test)
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
date '+%F %T' > .b573_t0.txt
uptime >> .b573_t0.txt
for S in A B C; do
  for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
    curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' -H 'Connection: close' 'https://search.kotobase.net/search?q=test' >> .b573_$S.ttfb
  done
done
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' -H 'Connection: close' 'https://kotobase.net/signup' >> .b573_ctl.ttfb
done
uptime >> .b573_t0.txt
date '+%F %T' >> .b573_t0.txt
