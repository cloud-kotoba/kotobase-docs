s = open('query-cosientist.md').read()
import re
# unique marker: run625A cold 5/20
for m in ['run625A cold 5/20', 'falsify 2026-09-15 (第253回']:
    idxs = [mm.start() for mm in re.finditer(re.escape(m), s)]
    print(m, '->', len(idxs), idxs[:6])
