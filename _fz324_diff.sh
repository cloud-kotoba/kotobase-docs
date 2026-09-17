#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== diffstat ==="
git diff --stat
echo "=== changed query-cosientist (context around KZ3 row tail) ==="
git diff -U0 query-cosientist.md | tail -20
} > /tmp/fz_diff.txt 2>&1
echo done