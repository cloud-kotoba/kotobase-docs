#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
F=query-cosientist.md
{
echo "=== top of Iteration log ==="
grep -n '^\- 2026-09-07: rank 第157回' "$F" | head -1
echo "=== order check (head entries) ==="
grep -n '^\- 2026-09-07: \(rank 第157回\|bench 第157回\|falsify 第166回\)' "$F" | head -5
echo "=== diff stat ==="
git diff --stat "$F"
echo "=== status ==="
git status --short -- "$F"
} > .b351_verify.txt 2>&1