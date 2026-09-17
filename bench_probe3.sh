#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
git fetch net-kotobase 2>&1
git log --oneline -3 net-kotobase/main 2>&1
echo "--- merge-base check"
git rev-list HEAD..net-kotobase/main --count 2>&1
