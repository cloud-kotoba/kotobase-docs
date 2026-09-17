#!/bin/sh
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b646_raw.txt
: > "$OUT"
TARGET='https://search.yataverse.com/search?q=test'
CONTROL='https://kotoba.cloud/'
for g in 1 2 3; do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$TARGET" >> "$OUT"
done
echo WARMUP_END >> "$OUT"
for run in A B C; do
  i=0
  while [ $i -lt 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$TARGET" >> "$OUT"
    i=$((i+1))
  done
  echo RUN_END_$run >> "$OUT"
done
i=0
while [ $i -lt 20 ]; do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$CONTROL" >> "$OUT"
  i=$((i+1))
done
echo ALL_END >> "$OUT"
date '+%H:%M:%S' >> "$OUT"
uptime | sed 's/.*load/load/' >> "$OUT"
