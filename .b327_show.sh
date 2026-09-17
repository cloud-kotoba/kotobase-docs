#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== show HEAD e97c6dd stat ==="
git show --stat e97c6dd 2>&1 | head -20
echo "=== show 4e66f3f stat ==="
git show --stat 4e66f3f 2>&1 | head -20
echo "=== show e97c6dd diff files ==="
git show --name-only e97c6dd 2>&1 | head -20
echo "=== grep rank list recent commits ==="
git log --oneline -40 2>&1 | grep -n "rank " | head -30