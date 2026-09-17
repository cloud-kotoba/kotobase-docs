#!/bin/bash
# cosientist K-Z3 19時台 n-add run497A-C + landing control (same established method)
# n=20 x3 + landing control, separate-connection curl, cold>=0.5s TTFB, nearest-rank p50
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/signup"
B=".b497"
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
: > "${B}_run.log"
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
date >> "${B}_run.log"
measure "A" "$URL_S"
echo "A done" >> "${B}_run.log"
measure "B" "$URL_S"
echo "B done" >> "${B}_run.log"
measure "C" "$URL_S"
echo "C done" >> "${B}_run.log"
measure "landing" "$URL_L"
echo "landing done" >> "${B}_run.log"
date >> "${B}_run.log"
echo "MEASURE_DONE" >> "${B}_run.log"