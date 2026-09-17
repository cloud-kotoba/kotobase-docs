#!/bin/sh
# falsify 第98回: K-Z3 17時台 n 積み増し run227A-C (n=20 x 3) + landing control (/signup)
# 同測定法: 別接続 curl, 正 endpoint search.kotobase.net/search?q=test, cold>=0.5s
OUT=_f98_run227_out.txt
: > $OUT
date '+%Y-%m-%dT%H:%M:%S%z' >> $OUT
for r in A B C; do
  i=0
  while [ $i -lt 20 ]; do
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "https://search.kotobase.net/search?q=test")
    echo "run227$r $t" >> $OUT
    i=$((i+1))
  done
  sleep 5
done
i=0
while [ $i -lt 20 ]; do
  t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "https://kotobase.net/signup")
  echo "control $t" >> $OUT
  i=$((i+1))
done
date '+%Y-%m-%dT%H:%M:%S%z' >> $OUT
echo "DONE" >> $OUT