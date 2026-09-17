#!/bin/bash
# K-Z3 13時台帯初計測 run561A-C, 同測定法: 別接続 curl, 正 endpoint search.kotobase.net/search?q=test, cold>=0.5s TTFB
# 3 warmup 除外 + n=20 sequential per run, landing control kotobase.net/signup
out=$1
for run in A B C; do
  for w in 1 2 3; do
    curl -o /dev/null -s --connect-timeout 10 "https://search.kotobase.net/search?q=test"
  done
  : > /tmp/b561_$run.txt
  for i in $(seq 1 20); do
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}' --connect-timeout 10 "https://search.kotobase.net/search?q=test")
    echo "$t" >> /tmp/b561_$run.txt
  done
done
: > /tmp/b561_ctrl.txt
for i in $(seq 1 20); do
  t=$(curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}' --connect-timeout 10 "https://kotobase.net/signup")
  echo "$t" >> /tmp/b561_ctrl.txt
done
echo "=== A ===" >> $out; cat /tmp/b561_A.txt >> $out
echo "=== B ===" >> $out; cat /tmp/b561_B.txt >> $out
echo "=== C ===" >> $out; cat /tmp/b561_C.txt >> $out
echo "=== CTRL ===" >> $out; cat /tmp/b561_ctrl.txt >> $out
date "+%Y-%m-%d %H:%M:%S %Z" >> $out
