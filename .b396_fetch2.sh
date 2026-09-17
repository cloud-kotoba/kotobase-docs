cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > .b396_fetch.txt 2>&1
echo "rc=$?" >> .b396_fetch.txt
echo "=== revs ===" >> .b396_fetch.txt
git rev-parse HEAD >> .b396_fetch.txt
git rev-parse net-kotobase/main >> .b396_fetch.txt
echo "=== log -8 ===" >> .b396_fetch.txt
git log --oneline -8 >> .b396_fetch.txt
echo "=== diffstat HEAD net-kotobase/main ===" >> .b396_fetch.txt
git diff --stat HEAD net-kotobase/main >> .b396_fetch.txt 2>&1
echo "=== status md ===" >> .b396_fetch.txt
git status --short query-cosientist.md >> .b396_fetch.txt
echo "=== is 0e98d28 ancestor of net-kotobase/main? ===" >> .b396_fetch.txt
git merge-base --is-ancestor 0e98d28 net-kotobase/main; echo "ancestor rc=$?" >> .b396_fetch.txt