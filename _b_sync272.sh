#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== remotes ==="
git remote -v
echo "=== all refs (main-ish) ==="
git for-each-ref --format='%(refname:short) %(objectname:short)' | grep -iE 'main|head' | head
echo "=== fetch net-kotobase ==="
git fetch net-kotobase 2>&1 | tail -3
echo "=== HEAD vs net-kotobase/main ==="
git rev-parse --short HEAD
git rev-parse --short net-kotobase/main 2>&1
echo "=== count divergence ==="
git rev-list --left-right --count HEAD...net-kotobase/main 2>&1