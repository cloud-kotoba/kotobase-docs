#!/bin/bash
# cosientist 第153回: K-Z3 13時台 n 積み増し run558A-C (同測定法 n=20 x3 + landing control)
OUT=/tmp/cosient_tick
mkdir -p "$OUT"
URL_S="https://search.kotobase.net/search?q=test"
URL_C="https://kotobase.net/signup"
for r in A B C; do
  f="$OUT/run558$r.txt"
  : > "$f"
  for i in $(seq 1 20); do
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --max-time 15 "$URL_S")
    echo "$t" >> "$f"
  done
  f2="$OUT/ctrl558.txt"
  : > "$f2"
  for i in $(seq 1 20); do
    t=$(curl -o /dev/null -s -w '%{http_code} %{time_total}' --max-time 15 "$URL_C")
    echo "$t" >> "$f2"
  done
done
uptime > "$OUT/uptime.txt"
