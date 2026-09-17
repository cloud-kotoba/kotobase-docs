#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== push attempt 1: net-kotobase HEAD:main ==="
git push net-kotobase HEAD:main 2>&1
echo "push1_rc=$?"