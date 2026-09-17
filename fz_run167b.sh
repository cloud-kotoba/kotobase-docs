#!/bin/bash
# falsify 第63回: K-Z3 20時台 n 積み増し run167A-C, same methodology (run166 準拠: TTFB + http_code)
OUT=fz_run167_out2.txt
: > $OUT
date >> $OUT
uptime >> $OUT
for run in A B C; do
  echo "=== run167$run search ===" >> $OUT
  for i in $(seq 1 20); do
    ttfb=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' --max-time 10 "https://search.kotobase.net/search?q=test")
    echo "167$run $i $ttfb" >> $OUT
  done
done
echo "=== landing control ===" >> $OUT
for i in $(seq 1 20); do
  ttfb=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' --max-time 10 "https://kotobase.net/")
  echo "LC $i $ttfb" >> $OUT
done
date >> $OUT
