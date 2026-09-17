cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== LOG ===" > /tmp/r_log2.txt
git log --oneline -8 >> /tmp/r_log2.txt 2>&1
echo "=== fold parent of ba7d904 ===" >> /tmp/r_log2.txt
git log --oneline ba7d904~1 >> /tmp/r_log2.txt 2>&1
echo "=== diff c313c5f..ba7d904 stat ===" >> /tmp/r_log2.txt
git diff --stat c313c5f..ba7d904 >> /tmp/r_log2.txt 2>&1
echo "=== does c313c5f contain rank120? ===" >> /tmp/r_log2.txt
git log --oneline --all --grep "rank 120" >> /tmp/r_log2.txt 2>&1