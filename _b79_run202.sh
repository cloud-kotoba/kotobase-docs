#!/bin/bash
# bench 第79回: K-Z3 10時台帯初計測 run202A-C + landing control
# 同一測定法: n=20 x 3 + control n=20, 別接続 curl (production HTTP, host load gate 外)
# endpoint: search.kotobase.net/search?q=test (正当 URL; kotobase.net/search は 404)
set -u
OUT=_b79_run202_out.txt
: > "$OUT"

url="https://search.kotobase.net/search?q=test"
ctrl="https://kotobase.net/signup"

for grp in 202A 202B 202C CTRL; do
  if [ "$grp" = "CTRL" ]; then u="$ctrl"; else u="$url"; fi
  echo "=== $grp ===" >> "$OUT"
  for i in $(seq 1 20); do
    t=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' --no-keepalive "$u")
    echo "$grp $i $t" >> "$OUT"
  done
done
echo "DONE" >> "$OUT"
date >> "$OUT"
