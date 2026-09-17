cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push net-kotobase HEAD:main > /tmp/kb_push.log 2>&1
echo "PUSH_RC=$?" >> /tmp/kb_push.log
git rev-parse HEAD >> /tmp/kb_push.log 2>&1
git fetch net-kotobase main >> /tmp/kb_push.log 2>&1
git rev-parse net-kotobase/main >> /tmp/kb_push.log 2>&1
echo done