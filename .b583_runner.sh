#!/bin/bash
# .b583_runner.sh — falsify K-Z3 15時台 n 積み増し run583A-C + landing control
set -u
PFX=/tmp/.b583
URL_S="https://search.kotobase.net/search?q=test"
URL_C="https://kotobase.net/signup"
rm -f /tmp/.b583_ts*.txt
for lab in A B C; do
  n=0
  while [ $n -lt 20 ]; do
    n=$((n+1))
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "$URL_S")
    echo "$lab $n $t" >> ${PFX}_search.tsv
  done
done
n=0
while [ $n -lt 20 ]; do
  n=$((n+1))
  t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "$URL_C")
  echo "CTL $n $t" >> ${PFX}_ctl.tsv
done
echo done > ${PFX}_done.txt
