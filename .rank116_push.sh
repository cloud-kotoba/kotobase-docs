#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== REMOTES ==="
git remote -v 2>&1
echo "=== CURRENT BRANCH ==="
git branch --show-current 2>&1
git rev-parse --abbrev-ref HEAD 2>&1
echo "=== HEAD ==="
git rev-parse HEAD 2>&1
echo "=== FETCH before push ==="
git fetch 2>&1
echo "fetch_rc=$?"
echo "=== REMOTE HEADS ==="
git for-each-ref --format='%(refname:short) %(objectname:short)' refs/remotes 2>&1
echo "=== push attempt: HEAD to main ==="
git push origin HEAD:main 2>&1
echo "push_rc=$?"
echo "=== HEAD after push ==="
git rev-parse HEAD 2>&1
echo "=== END ==="