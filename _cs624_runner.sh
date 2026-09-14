#!/bin/bash
# cosientist 第153回 K-Z3 2時台 n 積み増し run624A-C + landing control
# 同測定法: n=20 x3, 別接続 curl, cold>=0.5s (TTFB), 正 endpoint search.yataverse.com/search?q=test (301 読替後, search.kotobase.net → search.yataverse.com)
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for s in A B C; do
  : > _cs624_${s}.ttfb
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' \
      --max-time 15 'https://search.yataverse.com/search?q=test' >> _cs624_${s}.ttfb
  done
done
: > _cs624_landing.ttfb
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' \
    --max-time 15 'https://kotoba.cloud/' >> _cs624_landing.ttfb
done
echo DONE
