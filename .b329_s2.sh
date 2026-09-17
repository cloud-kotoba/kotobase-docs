cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== stat 0ca3490 ===" >> .b329_s2.txt
git show --stat --oneline 0ca3490 | head -30 >> .b329_s2.txt 2>&1
echo "=== files in repo root ===" >> .b329_s2.txt
git ls-tree --name-only HEAD | head -40 >> .b329_s2.txt 2>&1
echo "=== log: files changed in last 12 commits ===" >> .b329_s2.txt
git log --name-only --oneline -12 | grep -v '^$' | sort | uniq -c | sort -rn | head -20 >> .b329_s2.txt 2>&1
echo "=== branch ===" >> .b329_s2.txt
git branch -avv >> .b329_s2.txt 2>&1