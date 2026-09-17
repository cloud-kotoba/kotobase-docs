#!/bin/zsh
D=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
B=$D/.b596
mkdir -p $B
date '+%H:%M:%S' > $B/start.txt
curl -s -o $B/smoke_search.txt -w '%{http_code} %{time_total}\n' 'https://search.kotobase.net/search?q=test' > $B/smoke.txt
curl -s -o /dev/null -w '%{http_code}\n' 'https://kotobase.net/' >> $B/smoke.txt
curl -s -o /dev/null -w '%{http_code}\n' 'https://kotobase.net/signup' >> $B/smoke.txt
zts() { date '+%H:%M:%S'; }
for g in A B C; do
  f=$B/run596$g.raw
  : > $f
  i=0
  while (( i < 20 )); do
    t=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' 'https://search.kotobase.net/search?q=test')
    printf '%s %s\n' "$(zts)" "$t" >> $f
    (( i++ ))
  done
done
f=$B/control596.raw
: > $f
i=0
while (( i < 20 )); do
  t=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' 'https://kotobase.net/signup')
  printf '%s %s\n' "$(zts)" "$t" >> $f
  (( i++ ))
done
uptime >> $B/hostload.txt
date '+%H:%M:%S' > $B/end.txt
