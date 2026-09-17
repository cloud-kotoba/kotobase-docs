doc = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', encoding='utf-8').read()
lines = doc.split('\n')
out = []
# verify iter-log entry is now second line-ish (right after header)
for i, ln in enumerate(lines):
    if ln.startswith('## Iteration log'):
        out.append('iterlog header at line %d (1-based)' % (i + 1))
        out.append('NEXT after header (line %d):' % (i + 2))
        out.append(lines[i + 1][:140])
        break
# verify K-Z3 run403 evidence present at the L279 tail anchor
anchor = "A 両セット 7/20 散発/heavy で重複再現"
idx = doc.find(anchor)
out.append('anchor found:' + str(idx))
seg = doc[idx:idx + 120]
out.append('after-anchor segment: ' + seg)
out.append('run403 evidence present: %s' % ('run403' in doc))
out.append('run404 NEXT present: %s' % ('run404' in doc))
out.append('total_lines=%d' % len(lines))
open('/tmp/bench_verify.txt', 'w').write('\n'.join(out) + '\n')