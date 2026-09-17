cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch bench_fetch 2>&1 > /tmp/r209_fetch.txt
echo "===FETCH_RC===$?" > /tmp/r209_pre.txt
echo "===HEAD===" >> /tmp/r209_pre.txt
git rev-parse HEAD >> /tmp/r209_pre.txt 2>&1
echo "===REMOTE_bench===" >> /tmp/r209_pre.txt
git rev-parse bench_fetch/main >> /tmp/r209_pre.txt 2>&1
echo "===REMOTE_net===" >> /tmp/r209_pre.txt
git rev-parse net-kotobase/main >> /tmp/r209_pre.txt 2>&1
echo "===DIFF_STAT_qcm===" >> /tmp/r209_pre.txt
git diff HEAD --stat -- query-cosientist.md >> /tmp/r209_pre.txt 2>&1
echo "===HDR_COUNT===" >> /tmp/r209_pre.txt
python3 -c "d=open('query-cosientist.md').read(); print(d.count('## Iteration log'))" >> /tmp/r209_pre.txt 2>&1
echo "###DONE###" >> /tmp/r209_pre.txt