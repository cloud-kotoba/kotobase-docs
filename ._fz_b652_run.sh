#!/bin/bash
# falsify run652: K-Z3 11時台 n積み増し (production HTTP 実測, fallback)
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=._fz_b652_run_out.txt
: > "$OUT"
date >> "$OUT"
uptime >> "$OUT"
TARGET="https://search.yataverse.com/search?q=test"
CONTROL="https://kotoba.cloud/"
for set in A B C; do
  f=._fz_b652_search_$set.txt
  : > "$f"
  for i in 1 2 3; do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$TARGET" >> /dev/null
  done
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$TARGET" >> "$f"
  done
done
f=._fz_b652_control.txt
: > "$f"
for i in 1 2 3; do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$CONTROL" >> /dev/null
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "$CONTROL" >> "$f"
done
wc -l ._fz_b652_search_A.txt ._fz_b652_search_B.txt ._fz_b652_search_C.txt ._fz_b652_control.txt >> "$OUT"
date >> "$OUT"
