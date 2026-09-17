#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== FETCH ==="
git fetch 2>&1
echo "rc=$?"
echo "=== HEAD ==="
git rev-parse HEAD 2>&1
echo "=== UPSTREAM ==="
git rev-parse @{u} 2>&1
echo "=== LOG --oneline -15 ==="
git log --oneline -15 2>&1
echo "=== DIFF as of last rank (7429988..HEAD) ==="
git diff --stat 7429988..HEAD 2>&1
echo "=== DIFF since 8255634 (rank87) full summary ==="
git log --oneline --graph 8255634..HEAD 2>&1
echo "=== STATUS SHORT ==="
git status --short 2>&1
echo "=== END ==="