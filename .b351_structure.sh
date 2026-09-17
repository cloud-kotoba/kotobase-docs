#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== count '## Iteration log' in HEAD ==="
git show 7a0979c:query-cosientist.md | grep -c '^## Iteration log'
echo "=== entry order (first 6 bullets) in HEAD ==="
git show 7a0979c:query-cosientist.md | awk '/^## Iteration log/{f=1} f&&/^\- 2026-09-07:/{print NR": "$0}' | head -6 | cut -c1-70
echo "=== parent 44cddf9 '## Iteration log' count ==="
git show 44cddf9:query-cosientist.md | grep -c '^## Iteration log'
echo "=== HEAD file wc ==="
git show 7a0979c:query-cosientist.md | wc -l
} > .b351_structure.txt 2>&1