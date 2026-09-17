#!/bin/bash
# bench 第38回: K-Z2 発火直後 vs 経過後対比 n 増強 (rank 第37回 NEXT)
# cron */5 発火 04:35 直後 fire+~3s と fire+~90s の同測定法 n=20 対比 + landing control
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench38_run_out.txt"
: > "$OUT"
echo "start $(date)" >> "$OUT"
# wait until :35 boundary (fire+~3s)
while [ $(( $(date +%s) % 300 )) -lt 3 ] || [ $(( $(date +%s) % 300 )) -gt 30 ]; do sleep 1; done
echo "=== direct-after $(date) ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
done
# elapsed window: fire+~90s
while [ $(( $(date +%s) % 300 )) -lt 90 ]; do sleep 2; done
echo "=== elapsed $(date) ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
done
echo "=== landing control $(date) ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_L" >> "$OUT"
done
echo "end $(date)" >> "$OUT"
echo done
