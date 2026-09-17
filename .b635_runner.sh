#!/bin/bash
# K-Z3 23時台 n 積み増し run635A-C + landing control (kotoba.cloud/)
# 同測定法: n=20 x3, 別接続 curl, search endpoint + landing control 交互
OUT=.b635_run.txt
: > $OUT
SEARCH=https://search.yataverse.com/search?q=test
CTRL=https://kotoba.cloud/
for rep in 1 2 3; do
  # control 20 (先に landing で分離基盤確認)
  for i in $(seq 1 20); do
    r=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' --no-keepalive "$CTRL")
    echo "CTRL_$rep $i $r" >> $OUT
  done
  # search 20
  for i in $(seq 1 20); do
    r=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' --no-keepalive "$SEARCH")
    echo "SRCH_$rep $i $r" >> $OUT
  done
done
wc -l $OUT
