#!/bin/zsh
# falsify 第157回 K-Z3 11時台 run639A-C (n=20 x3 + landing control)
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b639_out
mkdir -p "$OUT"
URL_SEARCH="https://search.yataverse.com/search?q=test"
URL_CTRL="https://kotoba.cloud/"
for grp in A B C CTRL; do
  if [ "$grp" = "CTRL" ]; then URL=$URL_CTRL; else URL=$URL_SEARCH; fi
  f="$OUT/.b639_$grp.tsv"
  : > "$f"
  for i in $(seq 1 20); do
    t=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' --no-keepalive "$URL")
    printf '%s %s\n' "$i" "$t" >> "$f"
  done
done
python3 /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b639_stats.py
