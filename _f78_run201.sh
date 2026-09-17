#!/bin/sh
# falsify 78th tick: K-Z3 9時台 n 積み増し run201A-C (n=20 x 3) + landing control
OUT=_f78_run201_out.txt
: > $OUT
date '+%Y-%m-%dT%H:%M:%S%z' >> $OUT
for r in A B C; do
  i=0
  while [ $i -lt 20 ]; do
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "https://kotobase.net/search?q=test")
    echo "run201$r $t" >> $OUT
    i=$((i+1))
  done
  sleep 5
done
i=0
while [ $i -lt 20 ]; do
  t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "https://kotobase.net/signup")
  echo "control $t" >> $OUT
  i=$((i+1))
done
date '+%Y-%m-%dT%H:%M:%S%z' >> $OUT
