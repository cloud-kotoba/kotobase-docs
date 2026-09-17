#!/bin/bash
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b411_land.txt"
: > "$OUT"
CTRL="https://kotobase.net/signup"
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_total}\n" --max-time 30 "$CTRL" >> "$OUT" 2>&1
done
echo "land done: $(date '+%H:%M:%S')"