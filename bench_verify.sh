#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
grep -c "run156" query-cosientist.md > bench_verify.txt 2>&1
grep -n "bench 第50回" query-cosientist.md | sed -n '1,3p' >> bench_verify.txt
tail -5 query-cosientist.md >> bench_verify.txt
