#!/bin/bash
# cosientist K-Z3 17時台 n 積み増し run573A-C + landing control
# 同測定法: n=20 x3, 別接続 curl, cold>=0.5s (TTFB), endpoint search.kotobase.net/search?q=test
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
date '+run573 start %H:%M:%S' > _qc573_time.txt
for s in A B C; do
  : > _qc573_${s}.ttfb
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' \
      --max-time 15 'https://search.kotobase.net/search?q=test' >> _qc573_${s}.ttfb
  done
done
: > _qc573_landing.ttfb
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' \
    --max-time 15 'https://kotobase.net/signup' >> _qc573_landing.ttfb
done
date '+run573 end %H:%M:%S' >> _qc573_time.txt
echo DONE
