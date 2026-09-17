cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
ls -t .b46*.sh 2>/dev/null | head -5 > /tmp/kb_runner_ls.txt
ls -t .b193*.sh 2>/dev/null | head -5 >> /tmp/kb_runner_ls.txt
echo "===b467 files===" >> /tmp/kb_runner_ls.txt
ls -la .b467* 2>/dev/null >> /tmp/kb_runner_ls.txt
echo "===b468 files===" >> /tmp/kb_runner_ls.txt
ls -la .b468* 2>/dev/null >> /tmp/kb_runner_ls.txt
echo "===gitlog bench recent===" >> /tmp/kb_runner_ls.txt
git log --oneline -6 --grep="bench 第" >> /tmp/kb_runner_ls.txt 2>&1
echo done