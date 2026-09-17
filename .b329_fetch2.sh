cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > .b329_fetch.txt 2>&1
echo "rc=$?" >> .b329_fetch.txt
git rev-parse HEAD >> .b329_fetch.txt
git rev-parse net-kotobase/main >> .b329_fetch.txt
echo "=== log -6 ===" >> .b329_fetch.txt
git log --oneline -6 >> .b329_fetch.txt
echo "=== HEAD blob tail-30 ===" >> .b329_fetch.txt
git show HEAD:query-cosientist.md | tail -30 >> .b329_fetch.txt 2>&1
echo "=== status md ===" >> .b329_fetch.txt
git status --short query-cosientist.md >> .b329_fetch.txt 2>&1