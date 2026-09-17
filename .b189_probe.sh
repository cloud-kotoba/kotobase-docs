#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
{
echo "===GIT LOG bench/falsify/rank last 25==="
git log --oneline -25
echo "===run424 search==="
grep -rl "run424" . --include='.b*' 2>/dev/null | head -20
echo "===run423 search==="
grep -rl "run423" . --include='.b*' 2>/dev/null | head -20
echo "===HEAD qc K-Z3 row line numbers==="
git show HEAD:query-cosientist.md | grep -n "^| K-Z3" | tail -3
echo "===HEAD qc iteration log HEAD entry==="
git show HEAD:query-cosientist.md | grep -n "^\- 2026-09-0[78]\|^\- 2026-09-0[78]" | tail -3
echo "===HEAD qc total lines==="
git show HEAD:query-cosientist.md | wc -l
} > .b189_probe.txt 2>&1