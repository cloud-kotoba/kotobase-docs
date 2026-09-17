#!/bin/sh
# K-Z3 search cold-band n-add run432 (7時台帯 n 積み増し, 2026-09-08 falsify 第191回)
# production HTTP; separate curl connection per attempt; cold = time_starttransfer >= 0.5s
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
Q="https://search.kotobase.net/search?q=test"
CTRL="https://kotobase.net/signup"

run_one() {
  # $1 = outfileprefix, $2 = url
  f="$1"; u="$2"; i=1
  while [ "$i" -le 20 ]; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer} %{time_total}\n" "$u" >> "$f" 2>/dev/null
    i=$((i+1))
  done
}

run_one ".b432_run432_A.txt" "$Q"
run_one ".b432_run432_B.txt" "$Q"
run_one ".b432_run432_C.txt" "$Q"
run_one ".b432_run432_land.txt" "$CTRL"
echo "run432-DONE" > .b432_done.txt