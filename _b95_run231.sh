#!/bin/sh
# bench 第95回: K-Z3 18時台 n 積み増し run231A-C (n=20 x3) + landing control (/signup)
# 同測定法: 別接続 curl, 正 endpoint search.kotobase.net/search?q=test, cold>=0.5s TTFB
# production HTTP 実測のため gate 外 (host load 78-88 超過)
OUT=_b95_run231_out.txt
: > $OUT
date '+%Y-%m-%dT%H:%M:%S%z' >> $OUT
for r in A B C; do
  i=0
  while [ $i -lt 20 ]; do
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}' --connect-timeout 10 "https://search.kotobase.net/search?q=test")
    echo "run231$r $t" >> $OUT
    i=$((i+1))
  done
  sleep 5
done
i=0
while [ $i -lt 20 ]; do
  t=$(curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}' --connect-timeout 10 "https://kotobase.net/signup")
  echo "control $t" >> $OUT
  i=$((i+1))
done
date '+%Y-%m-%dT%H:%M:%S%z' >> $OUT
uptime >> $OUT
echo "DONE" >> $OUT