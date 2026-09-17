#!/bin/sh
# cosientist (コア): K-Z3 20時台 n 積み増し run243A-C (n=20 x 3) + landing control (/signup)
# 同測定法: 別接続 curl, 正 endpoint search.kotobase.net/search?q=test, cold>=0.5s
# rank 第106回 NEXT: K-Z3 20時台 run243 で通算 n を 300 に揃え確定
OUT=_co_run243_out.txt
: > $OUT
date '+%Y-%m-%dT%H:%M:%S%z' >> $OUT
for r in A B C; do
  i=0
  while [ $i -lt 20 ]; do
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "https://search.kotobase.net/search?q=test")
    echo "run243$r $t" >> $OUT
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