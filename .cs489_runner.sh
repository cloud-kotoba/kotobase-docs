#!/bin/bash
# cosientist K-Z3 18時台 n-add run489 (independent; run488 taken by falsify-218)
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/signup"
B="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.cs489"
: > "${B}_out.txt"
measure () {
  local lid="$1" url="$2"
  : > "${B}_${lid}.ttfb"
  : > "${B}_${lid}.code"
  for i in $(seq 1 20); do
    line=$(curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}" --max-time 30 "$url")
    code=${line%% *}
    ttfb=${line#* }
    printf "%s\n" "$ttfb" >> "${B}_${lid}.ttfb"
    printf "%s\n" "$code" >> "${B}_${lid}.code"
  done
}
measure "A" "$URL_S"
measure "B" "$URL_S"
measure "C" "$URL_S"
measure "landing" "$URL_L"
echo "MEASURE_DONE" > "${B}_out.txt"
date "+%Y-%m-%d %H:%M:%S %Z" > "${B}_t0.txt"