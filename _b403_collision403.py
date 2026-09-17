import re
doc = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', encoding='utf-8').read()
out = []
# find all lines mentioning run403 / run404
for i, ln in enumerate(doc.split('\n')):
    if 'run403' in ln or 'run404' in ln:
        # just show first 130 chars of each matching line
        out.append('L%d: %s' % (i + 1, ln[:130]))
# count occurrences
out.append('run403 count=%d' % doc.count('run403'))
out.append('run404 count=%d' % doc.count('run404'))
out.append('bench 第183回 present=%s' % ('bench 第183回' in doc))
out.append('falsify 第176回 present=%s' % ('falsify 第176回' in doc))
open('/tmp/bench_collision.txt', 'w').write('\n'.join(out) + '\n')