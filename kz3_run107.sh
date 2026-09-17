#!/bin/bash
# K-Z2 direct-after vs elapsed: run107 (n=20 x4 windows + landing control)
URL_S="https://search.kotobase.net/search?q=test"
URL_L="https://kotobase.net/"
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run107_out.txt"
: > "$OUT"
echo "start $(date)" >> "$OUT"
# wait until :00 of next 5-min boundary
while [ $(( $(date +%s) % 300 )) -ge 5 ]; do sleep 1; done
echo "=== run107A direct-after $(date) ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
done
# elapsed window: fire-time +90s
while [ $(( $(date +%s) % 300 )) -lt 90 ]; do sleep 2; done
echo "=== run107B elapsed $(date) ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
done
# wait until next boundary
while [ $(( $(date +%s) % 300 )) -ge 5 ]; do sleep 1; done
echo "=== run107C direct-after $(date) ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
done
while [ $(( $(date +%s) % 300 )) -lt 90 ]; do sleep 2; done
echo "=== run107D elapsed $(date) ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_S" >> "$OUT"
done
echo "=== landing control $(date) ===" >> "$OUT"
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "$URL_L" >> "$OUT"
done
echo "end $(date)" >> "$OUT"
echo done
