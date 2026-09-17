#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "falsify 第127回: K-Z3 1時台 run279A-C cold 2/60 (~3.3%), control 分離成立, 1時台通算 9/300" 2>&1
echo "commit_rc=$?"
echo "=== new HEAD ==="
git rev-parse HEAD