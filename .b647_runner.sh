#!/bin/zsh
# falsify run647A-C: K-Z3 23時台 2セット目 (9/16), n=20 x3 + landing control
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
TS=$(date +"%Y-%m-%dT%H:%M:%S%z")
echo "start=$TS" > "$OUT/.b647_meta.txt"
for grp in A B C; do
  : > "$OUT/.b647_$grp.csv"
  for i in $(seq 1 20); do
    r=$(curl -s -o /dev/null -w "%{http_code} %{time_total}" "https://search.yataverse.com/search?q=test")
    echo "$i,$r" >> "$OUT/.b647_$grp.csv"
  done
done
: > "$OUT/.b647_ctl.csv"
for i in $(seq 1 20); do
  r=$(curl -s -o /dev/null -w "%{http_code} %{time_total}" "https://kotoba.cloud/")
  echo "$i,$r" >> "$OUT/.b647_ctl.csv"
done
uptime >> "$OUT/.b647_meta.txt"
date +"end=%Y-%m-%dT%H:%M:%S%z" >> "$OUT/.b647_meta.txt"
