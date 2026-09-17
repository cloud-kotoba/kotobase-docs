#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== HEAD lines 361-368 (truncated 60) ==="
git show 7a0979c:query-cosientist.md | awk 'NR>=361 && NR<=368' | cut -c1-60 | head -8
echo "=== all '## Iteration log' line numbers in HEAD ==="
git show 7a0979c:query-cosientist.md | grep -n '^## Iteration log'
echo "=== parent 44cddf9 occurrence line ==="
git show 44cddf9:query-cosientist.md | grep -n '^## Iteration log'
} > .b351_dup.txt 2>&1