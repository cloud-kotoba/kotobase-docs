#!/bin/zsh
# K-Z3 15-ji-tai n tsumimashi run642A-C (n=20 x3 + landing control). 2026-09-16 15:2x JST.
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b642_out
mkdir -p "$OUT"
URL_SEARCH="https://search.yataverse.com/search?q=test"
URL_CTRL="https://kotoba.cloud/"
for grp in A B C CTRL; do
  if [ "$grp" = "CTRL" ]; then URL=$URL_CTRL; else URL=$URL_SEARCH; fi
  f="$OUT/.b642_$grp.tsv"
  : > "$f"
  for i in $(seq 1 20); do
    t=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' --no-keepalive --max-time 20 "$URL")
    printf '%s %s\n' "$i" "$t" >> "$f"
    sleep 0.2
  done
done
uptime > "$OUT/.b642_uptime.txt"
date '+%H:%M:%S' >> "$OUT/.b642_uptime.txt"
python3 /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b642_stats.py > "$OUT/.b642_stats_out.txt" 2>&1
