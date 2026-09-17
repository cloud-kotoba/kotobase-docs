cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for S in A B C; do
  for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
    curl -s -o /dev/null -w '%{time_starttransfer}\n' -H 'Connection: close' 'https://search.kotobase.net/search?q=test' >> .b558_$S.ttfb
  done
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' -H 'Connection: close' 'https://kotobase.net/signup' >> .b558_ctl.ttfb
done
