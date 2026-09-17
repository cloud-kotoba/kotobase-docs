#!/bin/sh
# bench K-Z3 深夜帯 n 積み増し, 同一測定法: n=20 x 3 run + landing control,
# 別接続 curl, threshold cold >= 0.5s TTFB.
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
TIMEFILE=$(date '+%Y%m%d_%H%M%S')
run_search _b_run258A.txt
run_search _b_run258B.txt
run_search _b_run258C.txt
run_land _b_land258.txt
date '+%Y-%m-%dT%H:%M:%S%z' > _b_run258_time.txt
echo "done" >> _b_run258_time.txt