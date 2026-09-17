#!/bin/bash
# falsify run551 K-Z3 11hr band n-add (2nd set) — n=20 x3 search + 20 control
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
U="https://search.kotobase.net/search?q=test"
C="https://kotobase.net/signup"
for lbl in A B C; do
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{time_starttransfer} %{http_code}\n" --max-time 15 "$U" >> .b551_run551${lbl}.ttfb
  done
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{time_starttransfer} %{http_code}\n" --max-time 15 "$C" >> .b551_run551_landing.ttfb
done
wc -l .b551_run551A.ttfb .b551_run551B.ttfb .b551_run551C.ttfb .b551_run551_landing.ttfb > .b551_run551_run.txt 2>&1
date "+%H:%M:%S" > .b551_run551_t0.txt
uptime >> .b551_run551_t0.txt
