#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase 2>&1
echo "=== HEAD ==="
git rev-parse HEAD
echo "=== remote main ==="
git rev-parse net-kotobase/main 2>&1
echo "=== run279 evidence occurrence (should be 1) ==="
grep -c "run279A" query-cosientist.md
echo "=== secret sweep (should be empty) ==="
grep -n -iE "sk-[a-z0-9]{12,}|bearer [a-zA-Z0-9._-]{20,}|PRIVATE KEY" query-cosientist.md | tail -3