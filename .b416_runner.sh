#!/bin/bash
# K-Z3 2時台(9/8) n積み増し run416A-C + landing control (bench 第187回)
# 別接続 curl, TTFB (time_starttransfer), cold>=0.5s
SEARCH="https://search.kotobase.net/search?q=test"
CTRL="https://kotobase.net/signup"
OUT="/tmp/b416"
mkdir -p "$OUT"

run_one() { # $1=outfile $2=url $3=n
  local f="$1" url="$2" n="$3" i
  : > "$f"
  for i in $(seq 1 "$n"); do
    curl -s -o /dev/null -w "%{time_starttransfer}\t%{time_total}\t%{http_code}\n" "$url" >> "$f"
  done
}

echo "START $(date '+%H:%M:%S')" > "$OUT/time.txt"
run_one "$OUT/A.txt" "$SEARCH" 20
echo "A done $(date '+%H:%M:%S')" >> "$OUT/time.txt"
run_one "$OUT/B.txt" "$SEARCH" 20
echo "B done $(date '+%H:%M:%S')" >> "$OUT/time.txt"
run_one "$OUT/C.txt" "$SEARCH" 20
echo "C done $(date '+%H:%M:%S')" >> "$OUT/time.txt"
run_one "$OUT/ctrl.txt" "$CTRL" 20
echo "CTRL done $(date '+%H:%M:%S')" >> "$OUT/time.txt"
echo "ALL DONE" >> "$OUT/time.txt"
