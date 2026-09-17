#!/bin/zsh
# falsify run626B: K-Z3 8時台 n accumulation. 2026-09-15 08:2x JST.
# A/B/C: search.yataverse.com query endpoint x20 each; CTL: landing control x20.
D=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for grp in A B C CTL; do
  F="$D/.b626_${grp}.csv"
  true > "$F"
  if [ "$grp" = "CTL" ]; then
    URL="https://kotobase.net/signup"
  else
    URL="https://search.yataverse.com/search?q=test"
  fi
  for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
    R=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' --max-time 20 "$URL")
    printf '%s,%s\n' "$i" "$R" >> "$F"
    sleep 0.4
  done
done
uptime > "$D/.b626_uptime.txt"
