#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===STATUS SHORT==="
git status --short
echo "===DIFF STAT query-cosientist.md vs HEAD==="
git diff HEAD --stat -- query-cosientist.md
echo "===LOG -3==="
git log --oneline -3
echo "===COUNT Iteration log header==="
grep -c "## Iteration log" query-cosientist.md
echo "===uptime==="
uptime
} > _rk_pre.txt 2>&1