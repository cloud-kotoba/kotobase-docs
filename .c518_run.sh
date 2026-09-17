#!/bin/sh
# cosientist 第151回: K-Z3 0時台(24時台) n 積み増し run518A-C + landing control
# 同一測定法: n=20 sequential per run, 別接続 curl (毎回新規プロセス=新規接続),
# TTFB (time_starttransfer) capture, cold>=0.5s, nearest-rank p50, 正 endpoint search?q=test
OUT=.c518_run.log
: > "$OUT"
echo "start $(date '+%Y-%m-%d %H:%M:%S %z')" >> "$OUT"
uptime >> "$OUT"
run_one() {
  local label="$1"; local url="$2"; local n="$3"; local fname="$4"
  : > "$fname"
  local i=1
  while [ "$i" -le "$n" ]; do
    curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' --max-time 15 "$url" >> "$fname"
    i=$((i+1))
    sleep 0.1
  done
  echo "$label done: $(wc -l < "$fname") samples" >> "$OUT"
}
SEARCH="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"
run_one "run518A" "$SEARCH" 20 .c518_A.txt
sleep 2
run_one "run518B" "$SEARCH" 20 .c518_B.txt
sleep 2
run_one "run518C" "$SEARCH" 20 .c518_C.txt
sleep 2
run_one "landing" "$CONTROL" 20 .c518_land.txt
echo "finish $(date '+%Y-%m-%d %H:%M:%S %z')" >> "$OUT"
uptime >> "$OUT"
# live smoke
: > .c518_smoke.txt
for u in "https://kotobase.net/" "https://kotobase.net/signup" "$SEARCH"; do
  curl -s -o /dev/null -w '%{http_code}\n' --max-time 15 "$u" >> .c518_smoke.txt
done