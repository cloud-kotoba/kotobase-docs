#!/bin/bash
# cosientist K-Z3 10時台 3セット目 run547A-C + landing control
# 同測定法: n=20 x3, 別接続 curl, cold>=0.5s (TTFB), endpoint search.kotobase.net/search?q=test
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for s in A B C; do
  : > _cos547_${s}.ttfb
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' \
      --max-time 15 'https://search.kotobase.net/search?q=test' >> _cos547_${s}.ttfb
  done
done
: > _cos547_landing.ttfb
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' \
    --max-time 15 'https://kotobase.net/signup' >> _cos547_landing.ttfb
done
echo DONE
