cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch bench_fetch 2>&1 > /tmp/r209_postfetch.txt
echo "===FETCH_RC===$?" > /tmp/r209_post.txt
echo "===HEAD===" >> /tmp/r209_post.txt
git rev-parse HEAD >> /tmp/r209_post.txt 2>&1
echo "===REMOTE_bench===" >> /tmp/r209_post.txt
git rev-parse bench_fetch/main >> /tmp/r209_post.txt 2>&1
echo "===REMOTE_net===" >> /tmp/r209_post.txt
git rev-parse net-kotobase/main >> /tmp/r209_post.txt 2>&1
echo "===BLOB_CHECK===" >> /tmp/r209_post.txt
git show HEAD:query-cosientist.md 2>/dev/null > /tmp/r209_committed.md
python3 -c "
d=open('/tmp/r209_committed.md').read()
print('hdr_count', d.count('## Iteration log'))
i=d.index('## Iteration log')
print('head_entry_prefix', repr(d[i:i+45]))
print('rank209_present', 'rank 第209回' in d)
print('bench193_after_rank209', d.index('rank 第209回') < d.index('bench 第193回。13:28'))
print('order_ok', d.index('- 2026-09-08: rank 第209回。') < d.index('- 2026-09-08: bench 第193回。13:28'))
" >> /tmp/r209_post.txt 2>&1
echo "###DONE###" >> /tmp/r209_post.txt