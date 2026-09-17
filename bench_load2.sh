#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
uptime > bench_load2.txt 2>&1
tail -2 kz3_run156_out.txt >> bench_load2.txt
