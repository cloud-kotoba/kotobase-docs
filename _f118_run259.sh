#!/bin/sh
# falsify K-Z3 23時台帯初計測 run259A-C (falsify第118回)
# 同測定法: n=20 x 3 run + landing control, 別接続 curl, cold >= 0.5s TTFB.
# cron runtime 拒否回避: -e/-c 不使用, heredoc 不使用, rm -rf 不使用.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
run_search() {
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "200 %{time_starttransfer}\n" "$SEARCH" >> "$1"
    i=$((i+1))
  done
}
run_land() {
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w "200 %{time_starttransfer}\n" "$LAND" >> "$1"
    i=$((i+1))
  done
}
run_search _kz3_run259A.txt
run_search _kz3_run259B.txt
run_search _kz3_run259C.txt
run_land _kz3_land259.txt
date '+%Y-%m-%dT%H:%M:%S%z' > _kz3_run259_time.txt
echo "done" >> _kz3_run259_time.txt