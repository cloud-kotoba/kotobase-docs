#!/bin/sh
# falsify 第128回: K-Z3 1時台深夜帯 n 積み増し run281A-C (n=20 x 3) + landing control (/signup)
# Method: n=20 x 3 + landing control, separate-connection curl, Tokyo,
# cold threshold time_total >= 0.5s. One request = one curl (fresh conn).
OUT=_f128_run281_out.txt
: > "$OUT"
date '+%Y-%m-%dT%H:%M:%S%z' >> "$OUT"
for r in A B C; do
  i=0
  while [ $i -lt 20 ]; do
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "https://search.kotobase.net/search?q=test")
    echo "run281$r $t" >> "$OUT"
    i=$((i+1))
    sleep 0.1
  done
  sleep 5
done
i=0
while [ $i -lt 20 ]; do
  t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --connect-timeout 10 "https://kotobase.net/signup")
  echo "control $t" >> "$OUT"
  i=$((i+1))
  sleep 0.1
done
date '+%Y-%m-%dT%H:%M:%S%z' >> "$OUT"
echo "DONE" >> "$OUT"