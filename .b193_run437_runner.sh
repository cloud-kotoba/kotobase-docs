#!/bin/bash
# K-Z3 6時台帯初計測 run425 — production HTTP 実測 (gate外), 別接続 curl, 同一測定法 (n=20 x3 + landing control)
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
export PATH="/usr/bin:/bin:/usr/sbin:/sbin"
OUT=.b193_run437
: > "$OUT"_A.txt; : > "$OUT"_B.txt; : > "$OUT"_C.txt; : > "$OUT"_landing.txt
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
# run A/B/C: 20 each + landing control 20
for tag in A B C; do
  for i in $(seq 1 20); do
    t=$(curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}" --max-time 30 "$SEARCH" 2>/dev/null)
    echo "$i $t" >> "$OUT"_$tag.txt
  done
done
for i in $(seq 1 20); do
  t=$(curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}" --max-time 30 "$LANDING" 2>/dev/null)
  echo "$i $t" >> "$OUT"_landing.txt
done
echo done