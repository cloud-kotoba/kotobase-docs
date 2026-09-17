#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git add query-cosientist.md
git commit -m "falsify 第239回: K-Z3 9時台帯初計測 run538 cold 0/60 (control 0/20), 完全静穏分離成立, iter/evidence 追記" > /tmp/b538_commit.txt 2>&1
echo "COMMIT_RC=$?" >> /tmp/b538_commit.txt
git rev-parse HEAD >> /tmp/b538_commit.txt