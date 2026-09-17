#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
git fetch net-kotobase main 2>&1 | tail -2
echo "=== remote top ==="
git log --oneline -2 net-kotobase/main
echo "=== HEAD ==="
git rev-parse HEAD
echo "=== diff stat (doc only) ==="
git diff --stat query-cosientist.md
} > .b327_precommit.txt 2>&1