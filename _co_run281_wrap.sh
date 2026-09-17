#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
sh _co_run281.sh
/usr/bin/python3 _co_stats281.py > _co_run281_stats.txt 2>&1
echo "==== time/codes ====" >> _co_run281_stats.txt
cat _co_run281_time.txt >> _co_run281_stats.txt 2>&1
echo "==== load1 ====" >> _co_run281_stats.txt
uptime >> _co_run281_stats.txt 2>&1
echo "==== smoke ====" >> _co_run281_stats.txt
curl -s -o /dev/null -w "search %{http_code}\n" "https://search.kotobase.net/search?q=test" >> _co_run281_stats.txt 2>&1
curl -s -o /dev/null -w "land %{http_code}\n" "https://kotobase.net/signup" >> _co_run281_stats.txt 2>&1
echo done281