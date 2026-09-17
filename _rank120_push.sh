cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push net-kotobase HEAD:main > /tmp/r_push.txt 2>&1
echo "PUSH_RC=$?" >> /tmp/r_push.txt
git rev-parse HEAD >> /tmp/r_push.txt
git rev-parse net-kotobase/main >> /tmp/r_push.txt