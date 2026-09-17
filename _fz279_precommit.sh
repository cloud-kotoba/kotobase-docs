#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== git status before commit ==="
git status --short | head -20
echo "=== ABS HEAD ==="
git rev-parse HEAD
echo "=== remote ==="
git rev-parse net-kotobase/main 2>&1