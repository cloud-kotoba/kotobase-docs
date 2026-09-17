#!/bin/zsh
set -u
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
D=_f251
mkdir -p $D
date '+%Y-%m-%d %H:%M:%S %Z' > $D/start_time.txt
uptime >> $D/start_time.txt
# live smoke 3 endpoints first (rank 261 directive)
curl -s -o /dev/null -w '%{http_code} %{time_total}\n' 'https://search.kotobase.net/search?q=test' > $D/smoke_search.txt
curl -s -o /dev/null -w '%{http_code} %{time_total}\n' 'https://kotobase.net/' > $D/smoke_root.txt
curl -s -o /dev/null -w '%{http_code} %{time_total}\n' 'https://kotobase.net/signup' > $D/smoke_signup.txt
cat $D/smoke_search.txt $D/smoke_root.txt $D/smoke_signup.txt > $D/smoke_all.txt
