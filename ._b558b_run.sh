#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=._b558b_out.txt
: > "$OUT"
date >> "$OUT"
for set in A B C; do
  f=._b558b_search_$set.txt
  : > "$f"
  for i in 1 2 3; do
    curl -s -o /dev/null "https://search.kotobase.net/search?q=test"
  done
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://search.kotobase.net/search?q=test" >> "$f"
  done
done
f=._b558b_control.txt
: > "$f"
for i in 1 2 3; do
  curl -s -o /dev/null "https://kotobase.net/signup"
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://kotobase.net/signup" >> "$f"
done
wc -l ._b558b_*.txt >> "$OUT"
date >> "$OUT"
