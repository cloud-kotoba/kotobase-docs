cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===HEAD===" > /tmp/rank_gitlog.txt
git rev-parse HEAD >> /tmp/rank_gitlog.txt 2>&1
echo "===LOG_15===" >> /tmp/rank_gitlog.txt
git log --oneline -20 >> /tmp/rank_gitlog.txt 2>&1
echo "===LOG_author_date_10===" >> /tmp/rank_gitlog.txt
git log -10 --format='%h %ad %s' --date=format:'%m-%d %H:%M:%S' >> /tmp/rank_gitlog.txt 2>&1