#!/bin/bash
# K-Z3 18時台 n 積み増し run161A-C, same methodology n=20 x 3 + landing control
OUT=fz_run161_out.txt
: > $OUT
SEARCH="https://kotobase.net/api/search?q=test"
date "+START %H:%M:%S %Z" >> $OUT
uptime >> $OUT
for R in A B C; do
  RAW=/tmp/fz161_$R.txt
  : > $RAW
  for i in $(seq 1 20); do
    T=$(curl -s -o /dev/null -w "%{time_total}" --max-time 10 "$SEARCH")
    echo "$i $T" >> $RAW
  done
  echo "== run161$R ==" >> $OUT
  python3 fz_stats.py $RAW >> $OUT
done
# landing control
RAW=/tmp/fz161_ctl.txt
: > $RAW
for i in $(seq 1 20); do
  T=$(curl -s -o /dev/null -w "%{time_total}" --max-time 10 "https://kotobase.net/")
  echo "$i $T" >> $RAW
done
echo "== landing control ==" >> $OUT
python3 fz_stats.py $RAW >> $OUT
date "+END %H:%M:%S" >> $OUT
