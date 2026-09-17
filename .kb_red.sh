cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > /tmp/kb_red.txt 2>&1
echo "FETCH_RC=$?" >> /tmp/kb_red.txt
git rev-parse HEAD >> /tmp/kb_red.txt 2>&1
git rev-parse net-kotobase/main >> /tmp/kb_red.txt 2>&1
echo "=== diff HEAD query-cosientist.md (should be empty) ===" >> /tmp/kb_red.txt
git diff HEAD -- query-cosientist.md 2>&1 | head -5 >> /tmp/kb_red.txt
echo done