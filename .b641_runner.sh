#!/bin/zsh
# K-Z3 14-ji-tai n tsumimashi run641A-C (n=20 x3 + landing control). 2026-09-16 14:1x JST.
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b641_out
mkdir -p "$OUT"
URL_SEARCH="https://search.yataverse.com/search?q=test"
URL_CTRL="https://kotoba.cloud/"
for grp in A B C CTRL; do
  if [ "$grp" = "CTRL" ]; then URL=$URL_CTRL; else URL=$URL_SEARCH; fi
  f="$OUT/.b641_$grp.tsv"
  : > "$f"
  for i in $(seq 1 20); do
    t=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' --no-keepalive --max-time 20 "$URL")
    printf '%s %s\n' "$i" "$t" >> "$f"
    sleep 0.2
  done
done
uptime > "$OUT/.b641_uptime.txt"
date '+%H:%M:%S' >> "$OUT/.b641_uptime.txt"
python3 /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b641_stats.py > "$OUT/.b641_stats_out.txt" 2>&1
