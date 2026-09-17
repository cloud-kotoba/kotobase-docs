#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== DATE ==="
date '+%Y-%m-%d %H:%M:%S %Z'
echo "=== UPTIME ==="
uptime
echo "=== GIT status ==="
git status --short
echo "=== in-flight b-files ==="
ls -1 .b349* 2>/dev/null || echo "no .b349 files"
ls -1 .b3*.py .b3*.sh .b3*.txt 2>/dev/null || echo "no b3x files"
echo "=== HEAD last1 ==="
git log --oneline -1
} > .b349_state.txt 2>&1