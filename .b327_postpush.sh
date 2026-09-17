#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
git fetch net-kotobase main 2>&1 | tail -2
echo "=== remote top 2 ==="
git log --oneline -2 net-kotobase/main
echo "=== status of doc ==="
git status --short query-cosientist.md
} > .b327_postpush.txt 2>&1