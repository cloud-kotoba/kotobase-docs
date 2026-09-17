#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -F .b457_msg.txt > .b457_commit.log 2>&1
echo "commit_rc=$?" > /tmp/b457_commit_rc.txt
git push net-kotobase HEAD:main > /tmp/b457_push.log 2>&1
echo "push_rc=$?" > /tmp/b457_push_rc.txt
exit 0