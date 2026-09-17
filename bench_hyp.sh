#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
grep -n "K-Z3" query-cosientist.md | sed -n '1,3p' > bench_hyp.txt
grep -n "open" query-cosientist.md | sed -n '1,8p' >> bench_hyp.txt
