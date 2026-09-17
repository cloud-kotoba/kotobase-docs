#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== files in bench 109 commit (32249e4) ==="
git show --stat --format='%s' 32249e4 | head -20
echo ""
echo "=== files in falsify 124 commit (3a19846) ==="
git show --stat --format='%s' 3a19846 | head -20