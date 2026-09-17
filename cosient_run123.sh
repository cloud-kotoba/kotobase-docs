#!/bin/bash
# K-Z3 9時台 n 積み増し run123A-C, same methodology n=20 x 3 + landing control
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
PY=/opt/homebrew/bin/python3
OUT=cosient_run123_out.txt
: > $OUT
SEARCH="https://kotobase.net/api/search?q=test"
date "+START %H:%M:%S %Z" >> $OUT
uptime >> $OUT
for R in A B C; do
  RAW=/tmp/cos123_$R.txt
  : > $RAW
  for i in $(seq 1 20); do
    T=$(curl -s -o /dev/null -w "%{time_total}" --max-time 10 "$SEARCH")
    echo "$i $T" >> $RAW
  done
  echo "== run123$R ==" >> $OUT
  $PY fz_stats.py $RAW >> $OUT
done
# landing control
RAW=/tmp/cos123_ctl.txt
: > $RAW
for i in $(seq 1 20); do
  T=$(curl -s -o /dev/null -w "%{time_total}" --max-time 10 "https://kotobase.net/")
  echo "$i $T" >> $RAW
done
echo "== landing control ==" >> $OUT
$PY fz_stats.py $RAW >> $OUT
date "+END %H:%M:%S" >> $OUT
