#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
date '+%Y-%m-%d %H:%M:%S' > .b651_t0.txt
uptime >> .b651_t0.txt
i=0
while [ $i -lt 20 ]; do
  curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://search.yataverse.com/search?q=test" >> .b651_A.txt
  i=$((i+1))
done
i=0
while [ $i -lt 20 ]; do
  curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://search.yataverse.com/search?q=test" >> .b651_B.txt
  i=$((i+1))
done
i=0
while [ $i -lt 20 ]; do
  curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://search.yataverse.com/search?q=test" >> .b651_C.txt
  i=$((i+1))
done
i=0
while [ $i -lt 20 ]; do
  curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}\n" "https://kotoba.cloud/" >> .b651_land.txt
  i=$((i+1))
done
date '+%Y-%m-%d %H:%M:%S' > .b651_t1.txt
uptime >> .b651_t1.txt
