#!/bin/sh
# falsify K-Z3 21hr band n-add run397 (n=20 x 3 + landing control), same method.
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
: > "$OUT/.f397_time.txt"
date '+start %Y-%m-%dT%H:%M:%S%z' >> "$OUT/.f397_time.txt"
uptime >> "$OUT/.f397_time.txt"
for run in A B C land; do
  case "$run" in
    A|B|C) url="$SEARCH" ;;
    land)  url="$LAND" ;;
  esac
  f="$OUT/.f397_397${run}.txt"
  : > "$f"
  i=0
  while [ "$i" -lt 20 ]; do
    line=$(curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}' --max-time 30 "$url")
    printf '%s\n' "$line" >> "$f"
    i=$((i+1))
  done
  echo "$run done: $(wc -l < "$f") rows"
done
date '+end %Y-%m-%dT%H:%M:%S%z' >> "$OUT/.f397_time.txt"
uptime >> "$OUT/.f397_time.txt"
echo DONE >> "$OUT/.f397_time.txt"