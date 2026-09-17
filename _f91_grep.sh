#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "---K-Z3 row (hypothesis table)---"
grep -n "^| K-Z3 " query-cosientist.md
echo "---rn230 regex across doc---"
grep -n "run23[0-9]" query-cosientist.md | tail -20
echo "---iteration log latest---"
grep -n "第10[0-9]回\|Iteration" query-cosientist.md | tail -10
echo "---recent lines mentioning 18時台---"
grep -n "18時台" query-cosientist.md | tail -10