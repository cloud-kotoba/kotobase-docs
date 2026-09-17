#!/bin/bash
# K-Z3 run456 measurement (10時台 n-add on 9/8): 3 sets n=20 search + landing control n=20 signup
# Method: curl separate connection, cold>=0.5s TTFB, nearest-rank p50, one HTTP request per iteration (contract n=20)
set -u
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
# live smoke (SOUL step 4)
echo -n "smoke /: " > "$OUT/.b456_smoke.txt"
curl -sS -o /dev/null -w "%{http_code}\n" "https://kotobase.net/" >> "$OUT/.b456_smoke.txt" 2>/dev/null
echo -n "smoke /signup: " >> "$OUT/.b456_smoke.txt"
curl -sS -o /dev/null -w "%{http_code}\n" "https://kotobase.net/signup" >> "$OUT/.b456_smoke.txt" 2>/dev/null
T0=$(date +%s%N)
for s in A B C; do
  echo -n > "$OUT/.b456_run456${s}_raw.ttfb"
  for i in $(seq 1 20); do
    curl -sS -o /dev/null \
      -w "%{http_code} %{time_starttransfer}\n" \
      "https://search.kotobase.net/search?q=test" >> "$OUT/.b456_run456${s}_raw.ttfb" 2>/dev/null
  done
done
# landing control
echo -n > "$OUT/.b456_landing_raw.ttfb"
for i in $(seq 1 20); do
  curl -sS -o /dev/null \
    -w "%{http_code} %{time_starttransfer}\n" \
    "https://kotobase.net/signup" >> "$OUT/.b456_landing_raw.ttfb" 2>/dev/null
done
T1=$(date +%s%N)
echo "elapsed_ms=$(( (T1-T0)/1000000 ))" > "$OUT/.b456_elapsed.txt"
date '+%Y-%m-%d %H:%M:%S JST' > "$OUT/.b456_t0.txt"
uptime > "$OUT/.b456_uptime.txt" 2>/dev/null
echo done