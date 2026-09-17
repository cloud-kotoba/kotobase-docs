#!/bin/sh
# K-Z3 7時台 run613A-C + landing control (falsify, 2026-09-14)
cd "$(dirname "$0")"
EP="https://search.kotobase.net/search?q=test"
LP="https://kotobase.net/signup"
for g in A B C; do
  : > ".f613_run613$g.ttfb"
  i=0
  while [ $i -lt 20 ]; do
    curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}\n' "$EP" >> ".f613_run613$g.ttfb"
    i=$((i+1))
  done
done
: > ".f613_ctl.ttfb"
i=0
while [ $i -lt 20 ]; do
  curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}\n' "$LP" >> ".f613_ctl.ttfb"
  i=$((i+1))
done
uptime > ".f613_uptime.txt"
