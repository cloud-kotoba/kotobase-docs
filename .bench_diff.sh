#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== DIFF STAT ==="
git diff --stat
echo "=== DIFF (only tracked) ==="
git diff -- query-cosientist.md | head -80
} > /tmp/bench_diff.txt 2>&1
echo done