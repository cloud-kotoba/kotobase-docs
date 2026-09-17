cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== verify run396 evidence in L279 ===" > .b396_verify.txt
python3 -c "
s=open('query-cosientist.md',encoding='utf-8').read()
print('run396 in file:', s.count('run396'))
print('bench 第177回 in file:', s.count('bench 第177回'))
i=s.find('run396A')
print('context:', s[i-40:i+200])
" >> .b396_verify.txt 2>&1
echo "=== status ===" >> .b396_verify.txt
git status --short query-cosientist.md >> .b396_verify.txt
echo "=== git diff stat ===" >> .b396_verify.txt
git diff --stat query-cosientist.md >> .b396_verify.txt
git diff --cached --stat >> .b396_verify.txt 2>&1