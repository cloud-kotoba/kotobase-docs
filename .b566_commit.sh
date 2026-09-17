cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m 'falsify 第252回: K-Z3 13時台 n 積み増し run566A-C cold 4/60, control 非静穏 (evidence + iter-log)' > /tmp/.b566_commit.txt 2>&1
git fetch net-kotobase > /dev/null 2>&1
git rev-parse HEAD >> /tmp/.b566_commit.txt
git rev-parse net-kotobase/main >> /tmp/.b566_commit.txt
git push net-kotobase HEAD:main >> /tmp/.b566_commit.txt 2>&1
git fetch net-kotobase > /dev/null 2>&1
git rev-parse HEAD >> /tmp/.b566_commit.txt
git rev-parse net-kotobase/main >> /tmp/.b566_commit.txt
