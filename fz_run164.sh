#!/bin/bash
# falsify 第61回: K-Z3 19時台 n 積み増し run164A-C, same methodology n=20 x 3 + landing control
OUT=fz_run164_out.txt
: > $OUT
SEARCH="https://kotobase.net/api/search?q=test"
date "+START %H:%M:%S %Z" >> $OUT
uptime >> $OUT
for R in A B C; do
  RAW=/tmp/fz164_$R.txt
  : > $RAW
  for i in $(seq 1 20); do
    T=$(curl -s -o /dev/null -w "%{time_total}" --max-time 10 "$SEARCH")
    echo "$i $T" >> $RAW
  done
  echo "== run164$R ==" >> $OUT
  python3 fz_stats.py $RAW >> $OUT
done
# landing control
RAW=/tmp/fz164_ctl.txt
: > $RAW
for i in $(seq 1 20); do
  T=$(curl -s -o /dev/null -w "%{time_total}" --max-time 10 "https://kotobase.net/")
  echo "$i $T" >> $RAW
done
echo "== landing control ==" >> $OUT
python3 fz_stats.py $RAW >> $OUT
date "+END %H:%M:%S" >> $OUT
