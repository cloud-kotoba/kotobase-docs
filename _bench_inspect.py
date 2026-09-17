wt = open('query-cosientist.md').read()
out = []
# find section header lines (non-indented, start of line)
import re
for i, ln in enumerate(wt.split('\n')):
    s = ln.strip()
    if s.startswith('#') or (len(s) < 120 and re.match(r'^(==+|=+|\*\*|#{1,6} )', s)):
        out.append('line %d: %s' % (i+1, s[:100]))
    elif re.match(r'^##? ', ln):
        out.append('line %d: %s' % (i+1, ln[:100]))
out.append('=== total entry-start line numbers ===')
starts = [(m.start(), m.group(0)) for m in re.finditer(r'\n- (?:2026-09-06: )?(?:rank|bench|falsify) 第9\d回', wt)]
for (pos, txt) in starts:
    line = wt[:pos].count('\n') + 1
    out.append('  line %d: %s' % (line, txt.strip()))
open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_bench_inspect_out.txt', 'w').write('\n'.join(out))
print('done')