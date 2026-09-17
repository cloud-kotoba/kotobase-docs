#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
grep -n "K-Z3" query-cosientist.md | tail -30 > bench_kz3.txt 2>&1
grep -c "" query-cosientist.md >> bench_kz3.txt
