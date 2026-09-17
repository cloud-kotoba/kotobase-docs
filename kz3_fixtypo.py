import sys
p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
bad = '\u5b8c\u5168\u9759\u7a42'  # 完全静穂 (typo)
good = '\u5b8c\u5168\u9759\u7a4f'  # 完全静穏
n = s.count(bad)
s = s.replace(bad, good)
s = s.replace('\u3002\n\n\nfalsify 2026-09-04 (K-Z3 \u591c\u5e2f 22\u6642\u53f0', '\u3002\n\nfalsify 2026-09-04 (K-Z3 \u591c\u5e2f 22\u6642\u53f0')
open(p, 'w', encoding='utf-8').write(s)
sys.stdout.write("fixed " + str(n) + "\n")
