#!/bin/sh
# K-Z3 20hr n-add run395: separate-connection curl, TTFB=time_starttransfer, n=20 each.
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for run in A B C land; do
  case "$run" in
    A|B|C) url="$SEARCH" ;;
    land)  url="$LAND" ;;
  esac
  f="$OUT/.b395_395${run}.txt"
  : > "$f"
  i=0
  while [ "$i" -lt 20 ]; do
    line=$(curl -s -o /dev/null -w '%{time_starttransfer}\t%{http_code}\n' --max-time 30 "$url")
    printf '%s\n' "$line" >> "$f"
    i=$((i+1))
  done
  echo "$run done: $(wc -l < "$f") rows"
done