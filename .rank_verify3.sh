#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===NUMSTAT==="
git diff HEAD --numstat -- query-cosientist.md
echo "===HEADER-COUNT==="
grep -c "^## Iteration log" query-cosientist.md
echo "===HDR==="
grep -n "^## Iteration log" query-cosientist.md | head -1
echo "===LINES-374-377==="
sed -n '374,377p' query-cosientist.md | cut -c1-60
echo "===STATUS==="
git status --short -- query-cosientist.md
echo "===DONE==="