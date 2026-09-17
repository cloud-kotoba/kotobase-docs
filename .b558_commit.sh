cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m 'falsify 第248回: K-Z3 12時台 2セット目 run558A-C cold 3/60, control 分離成立 (evidence + iter-log)' > /tmp/.b558_commit.txt 2>&1
git fetch net-kotobase > /dev/null 2>&1
git rev-parse HEAD >> /tmp/.b558_commit.txt
git rev-parse net-kotobase/main >> /tmp/.b558_commit.txt
