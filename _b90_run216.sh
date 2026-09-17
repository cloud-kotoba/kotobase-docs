#!/bin/sh
# bench 第90回 K-Z3 15時台 n 積み増し run216A-C (15時台 2セット目) + landing control
# 同一測定法: n=20 x 3 run, 別接続 curl, threshold cold >= 0.5s TTFB
# cron runtime 拒否回避: -e/-c 不使用, heredoc 不使用, rm -rf 不使用
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
run_search _b90_run216A.txt
run_search _b90_run216B.txt
run_search _b90_run216C.txt
run_land _b90_land216.txt
date '+%Y-%m-%dT%H:%M:%S%z' > _b90_time.txt
echo "run rc=$?" >> _b90_time.txt