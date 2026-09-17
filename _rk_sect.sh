#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===ITERATION LOG GREP==="
grep -n "## Iteration log" query-cosientist.md
echo "===ITERLOG HEAD (first 40 lines after header)==="
awk '/## Iteration log/{found=1} found{print NR": "$0}' query-cosientist.md | head -40
} > _rk_sect.txt 2>&1