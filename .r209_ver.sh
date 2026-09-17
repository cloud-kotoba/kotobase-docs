cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===HDR_COUNT===" > /tmp/r209_ver.txt
python3 -c "d=open('query-cosientist.md').read(); print(d.count('## Iteration log'))" >> /tmp/r209_ver.txt
echo "===RANK209_PRESENT===" >> /tmp/r209_ver.txt
python3 -c "d=open('query-cosientist.md').read(); print('rank 第209回' in d, 'run467' in d)" >> /tmp/r209_ver.txt
echo "===DIFF_NUMSTAT===" >> /tmp/r209_ver.txt
git diff HEAD --numstat -- query-cosientist.md >> /tmp/r209_ver.txt 2>&1
echo "===HEAD_ENTRY_HEAD===" >> /tmp/r209_ver.txt
python3 -c "d=open('query-cosientist.md').read(); i=d.index('## Iteration log'); print(d[i:i+120])" >> /tmp/r209_ver.txt
echo "###DONE###" >> /tmp/r209_ver.txt