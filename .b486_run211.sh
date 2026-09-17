#!/bin/bash
# bench 第211回 K-Z3 17時台 n-add run486A-C + landing control
# 同測定法: n=20 x3 + landing control, 別接続 curl, cold>=0.5s TTFB, nearest-rank p50
# endpoint: search.kotobase.net/search?q=test ; control: kotobase.net/signup
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/signup"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b486_out.txt"
B=".b486"
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
: > "$B_out.txt"
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
echo "MEASURE_DONE"