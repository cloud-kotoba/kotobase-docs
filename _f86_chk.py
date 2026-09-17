import io

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'

with io.open(src, encoding='utf-8') as f:
    t = f.read()

out = []
out.append('run211 occurrences: %d' % t.count('run211'))
out.append('run212 occurrences: %d' % t.count('run212'))
out.append('第86回 occurrences: %d' % t.count('第86回'))
out.append('K-Z3 row contains 14時台: %s' % ('14時台帯初計測' in t))
out.append('log line present: %s' % ('- 2026-09-06: falsify 第86回' in t))

with io.open('/tmp/_f86_chk_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
