doc = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', encoding='utf-8').read()
lines = doc.split('\n')
out = []
# find my bench 第183回 iter-log entry
for i, ln in enumerate(lines):
    if ln.startswith('- 2026-09-07: bench 第183回'):
        out.append('bench183 at L%d (first 200): %s' % (i + 1, ln[:200]))
        out.append('bench183 mentions run404: %s' % ('run404' in ln))
        out.append('bench183 mentions run403: %s' % ('run403' in ln))
        out.append('bench183 NEXT run405: %s' % ('run405' in ln))
        break
# K-Z3 evidence row: show tail
idx = doc.find('A 両セット 7/20 散発/heavy で重複再現')
seg = doc[idx:idx + 400]
out.append('KZ3 evidence after anchor: %s' % seg)
out.append('run404 ev present: %s' % ('run404' in doc))
out.append('run405 present: %s' % ('run405' in doc))
open('/tmp/bench_verify2.txt', 'w').write('\n'.join(out) + '\n')