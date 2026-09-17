#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== FETCH ==="
git fetch 2>&1
echo "rc=$?"
echo "=== HEAD ==="
git rev-parse HEAD 2>&1
echo "=== HEAD subject ==="
git log -1 --format='%s' 2>&1
echo "=== REMOTE MAIN ==="
git rev-parse refs/remotes/origin/main 2>&1
echo "=== IS HEAD == origin/main ? ==="
cmp <(git rev-parse HEAD) <(git rev-parse refs/remotes/origin/main) && echo EQUAL || echo DIFFER
echo "=== STATUS SHORT (tracked changes only) ==="
git status --short query-cosientist.md 2>&1
git diff --stat 2>&1
echo "=== WORKING TREE vs HEAD diff on md ==="
git diff HEAD -- query-cosientist.md | head -60 2>&1
echo "=== line count now ==="
wc -l query-cosientist.md 2>&1
echo "=== END ==="