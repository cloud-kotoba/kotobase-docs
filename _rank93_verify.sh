#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase 2>&1
echo "===remote top==="
git log --oneline -1 net-kotobase/main
echo "===local==="
git log --oneline -1
echo "===ahead/behind of remote==="
echo "local..remote:"; git rev-list --count HEAD..net-kotobase/main 2>&1
echo "remote..local:"; git rev-list --count net-kotobase/main..HEAD 2>&1