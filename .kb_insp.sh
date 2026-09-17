cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== .b468_A.ttfb ===" > /tmp/kb_inspect.txt
cat .b468_A.ttfb 2>&1 >> /tmp/kb_inspect.txt
echo "" >> /tmp/kb_inspect.txt
echo "=== .b468_t0.txt ===" >> /tmp/kb_inspect.txt
cat .b468_t0.txt 2>&1 >> /tmp/kb_inspect.txt
echo "" >> /tmp/kb_inspect.txt
echo "=== .b468_runner.sh ===" >> /tmp/kb_inspect.txt
cat .b468_runner.sh 2>&1 >> /tmp/kb_inspect.txt
echo "" >> /tmp/kb_inspect.txt
echo "=== git diff query-cosientist.md ===" >> /tmp/kb_inspect.txt
git diff HEAD -- query-cosientist.md 2>&1 | head -40 >> /tmp/kb_inspect.txt
echo "" >> /tmp/kb_inspect.txt
echo "=== git status short ===" >> /tmp/kb_inspect.txt
git status --short 2>&1 | grep -v "^\?\?" | head -20 >> /tmp/kb_inspect.txt
echo done