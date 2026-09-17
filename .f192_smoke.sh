#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for u in https://kotobase.net/ https://kotobase.net/signup; do
  curl -s -o /dev/null -w "%{http_code}\n" "$u" >> .f192_smoke.txt
done
uptime >> .f192_smoke.txt
date '+%H:%M:%S %Z' >> .f192_smoke.txt