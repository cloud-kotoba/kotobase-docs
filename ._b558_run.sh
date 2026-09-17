#!/bin/bash
# K-Z3 20時台 production HTTP 実測 (fallback, rank NEXT 委ねる)
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=._b558_out.txt
: > "$OUT"
date >> "$OUT"
uptime >> "$OUT"
for set in A B C; do
  f=._b558_search_$set.txt
  : > "$f"
  # 3 warmup (excluded)
  for i in 1 2 3; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://kotobase.net/search?q=test" >> /dev/null
  done
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://kotobase.net/search?q=test" >> "$f"
  done
done
f=._b558_control.txt
: > "$f"
for i in 1 2 3; do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://kotobase.net/signup" >> /dev/null
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://kotobase.net/signup" >> "$f"
done
wc -l ._b558_*.txt >> "$OUT"
date >> "$OUT"
