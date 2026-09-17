#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== my commit stat ==="
git show --stat --oneline 7a0979c | head -20
echo "=== added lines (first 90 chars each) ==="
git show 7a0979c -- query-cosientist.md | grep '^+' | grep -v '^+++' | cut -c1-90
echo "=== rank157 present in HEAD? (count) ==="
git show 7a0979c:query-cosientist.md | grep -c '^\- 2026-09-07: rank 第157回。14:59 JST tick'
echo "=== worktree status (query-cosientist.md) ==="
git status --short -- query-cosientist.md
echo "=== worktree diff vs HEAD numstat ==="
git diff --numstat HEAD -- query-cosientist.md
} > .b351_audit.txt 2>&1