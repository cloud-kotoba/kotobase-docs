#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
ls -la > bench_ls.txt 2>&1
wc -l query-cosientist.md >> bench_ls.txt 2>&1
head -60 query-cosientist.md >> bench_ls.txt
