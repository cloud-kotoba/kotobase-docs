cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== status md ===" >> .b329_md.txt
git status --short query-cosientist.md >> .b329_md.txt 2>&1
echo "=== HEAD rev ===" >> .b329_md.txt
git rev-parse HEAD >> .b329_md.txt 2>&1
echo "=== blob tail lines ===" >> .b329_md.txt
git show HEAD:query-cosientist.md | wc -l >> .b329_md.txt 2>&1
echo "=== blob last 20 lines ===" >> .b329_md.txt
git show HEAD:query-cosientist.md | tail -20 >> .b329_md.txt 2>&1
echo "=== disk wc ===" >> .b329_md.txt
wc -l query-cosientist.md >> .b329_md.txt 2>&1
echo "=== disk tail 12 ===" >> .b329_md.txt
tail -12 query-cosientist.md >> .b329_md.txt 2>&1