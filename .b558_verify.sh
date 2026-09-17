cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase > /dev/null 2>&1
git rev-parse HEAD net-kotobase/main > /tmp/.b558_verify.txt
grep -c 'falsify 第248回' query-cosientist.md >> /tmp/.b558_verify.txt
