#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===LINE-TOTAL==="
wc -l query-cosientist.md
echo "===HYPOTHESIS-TABLE (grep K-Q1/K-S1/K-Z2/K-Z3 header rows)==="
grep -n "^\| K-Q1\|^\| K-S1\|^\| K-S2\|^\| K-Z2\|^\| K-Z3" query-cosientist.md
echo "===RANK-HEADER-LINE==="
grep -n "rank 第1[0-9][0-9]回\|第1[0-9][0-9]回.*人口\|仮説数\|Population" query-cosientist.md | head -20
echo "===DONE==="