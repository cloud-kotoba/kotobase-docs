#!/bin/bash
# K-Z3 production HTTP measurement: n=20 x 3 + landing control, separate connections
# single -w per curl combining http_code and ttfb
TS0=$(date '+%H:%M:%S')
: > .b580_run580_t0.txt
echo "$TS0" > .b580_run580_t0.txt

for g in A B C; do
  : > .b580_run580_$g.txt
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://search.kotobase.net/search?q=test" >> .b580_run580_$g.txt
  done
done
: > .b580_run580_ctl.txt
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://kotobase.net/signup" >> .b580_run580_ctl.txt
done
date '+%H:%M:%S' > .b580_run580_t1.txt
uptime > .b580_run580_load.txt
echo done > .b580_run580_done.txt
