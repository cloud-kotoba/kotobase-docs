#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
sed -n '207p' query-cosientist.md | tail -c 700 > bench_verify2.txt
git diff --stat >> bench_verify2.txt
