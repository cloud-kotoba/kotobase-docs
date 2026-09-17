#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
sed -n '207p' query-cosientist.md | tail -c 600 > bench_rowtail.txt
