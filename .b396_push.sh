cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== push ===" > .b396_push.txt
git push net-kotobase HEAD:main >> .b396_push.txt 2>&1
echo "push rc=$?" >> .b396_push.txt
git rev-parse net-kotobase/main >> .b396_push.txt 2>&1
echo "=== verify remote head ===" >> .b396_push.txt
git log --oneline -3 net-kotobase/main >> .b396_push.txt 2>&1