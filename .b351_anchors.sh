#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
F=query-cosientist.md
{
echo "=== line count ==="
wc -l "$F"
echo "=== Iteration log anchor ==="
grep -n '^## Iteration log' "$F"
echo "=== rank 15x entries ==="
grep -n '^\- 2026-09-07: rank 第15[0-9]回' "$F"
echo "=== rank ordering line (rank 期待) ==="
grep -n 'rank (期待 gain' "$F"
echo "=== header rank 第 ==="
grep -n '^rank (期待 gain' "$F"
echo "=== K-Z3 / K-Q1 rows ==="
grep -n '^| K-' "$F"
} > .b351_anchors.txt 2>&1