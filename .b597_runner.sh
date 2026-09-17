#!/bin/sh
# run597A-C: K-Z3 23時台 n 積み増し (n=20 x3 + landing control), 別接続 curl
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b597
mkdir -p "$OUT"
for grp in A B C; do
  for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
    curl -sS -o /dev/null -w "%{http_code} %{time_total} %{time_starttransfer}\n" \
      "https://kotobase.net/api/search?q=test" >> "$OUT/b597_$grp.tsv"
  done
done
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
  curl -sS -o /dev/null -w "%{http_code} %{time_total} %{time_starttransfer}\n" \
    "https://kotobase.net/signup" >> "$OUT/b597_landing.tsv"
done
date -u +"%Y-%m-%dT%H:%M:%SZ" >> "$OUT/meta.txt"
