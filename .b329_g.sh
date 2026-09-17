cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== on-disk grep 第169回/run395/第168回 ===" > .b329_g.txt
grep -n "run39[2-9]\|第16[7-9]回\|第17[0-9]回" query-cosientist.md | head -40 >> .b329_g.txt
echo "=== on-disk line count ===" >> .b329_g.txt
wc -l query-cosientist.md >> .b329_g.txt
echo "=== HEAD blob grep run39x ===" >> .b329_g.txt
git show HEAD:query-cosientist.md | grep -n "run39[2-9]\|第16[7-9]回" | head -30 >> .b329_g.txt 2>&1
echo "=== iter-log markers count in HEAD blob ===" >> .b329_g.txt
git show HEAD:query-cosientist.md | grep -c "第16[0-9]回\|第17[0-9]回" >> .b329_g.txt 2>&1
echo "=== ls-files (tracked) count ===" >> .b329_g.txt
git ls-files | wc -l >> .b329_g.txt
echo "=== docs state files ===" >> .b329_g.txt
git ls-files | grep -i "state\|co-sientist\|query\|rank\|istanbul" | head -30 >> .b329_g.txt