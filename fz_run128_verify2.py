p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
needle = 'falsify 2026-09-05 (K-Z3 12時台 n 積み増し run128A'
assert needle in s
# Verify no secret-like patterns in appended area
i = s.find(needle)
seg = s[i:i+1200]
import re
bad = re.findall(r'(?i)(token|cookie|bearer|credential|password|PRIVATE KEY)', seg)
print('found; secret-pattern hits:', bad)
