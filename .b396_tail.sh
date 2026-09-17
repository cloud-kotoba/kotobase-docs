cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== disk line 279 tail 1200 chars ===" > .b396_tail.txt
python3 -c "
lines=open('query-cosientist.md',encoding='utf-8').read().split('\n')
s=lines[278]
print('L279 chars:',len(s))
print(s[-1200:])
" >> .b396_tail.txt 2>&1
echo "=== iter-log head (first 6 lines of L368-) ===" >> .b396_tail.txt
python3 -c "
lines=open('query-cosientist.md',encoding='utf-8').read().split('\n')
for i in range(367,373):
    print(f'L{i+1} chars={len(lines[i])} head={lines[i][:80]}')
" >> .b396_tail.txt 2>&1
echo "=== status ===" >> .b396_tail.txt
git status --short query-cosientist.md >> .b396_tail.txt 2>&1
git rev-parse HEAD >> .b396_tail.txt 2>&1
git rev-parse net-kotobase/main >> .b396_tail.txt 2>&1