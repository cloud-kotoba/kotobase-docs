src = open('query-cosientist.md', encoding='utf-8').read()
# The log entry still shows 现在時刻帯 with mixed forms. Fix exact substring.
bad1 = 'K-Z3 \u73b0\u5728\u6642\u523b\u5e26 n \u7a4d\u307f\u5897\u3057'
print('bad1 count:', src.count(bad1))
src = src.replace(bad1, 'K-Z3 \u73fe\u5728\u6642\u523b\u5e26 n \u7a4d\u307f\u5897\u3057')
bad2 = '\u5b8c\u5168\u9759\u7a33\u3060\u304c'
print('bad2 (静稳) count in file:', src.count('\u9759\u7a33'))
# also fix 静稳 -> 静穏 only inside our entry (j..j+300)
j = src.find('- 2026-09-05: falsify \u7b2c63\u56de')
k = src.find('\n', j)
entry = src[j:k]
fixed = entry.replace('\u9759\u7a33', '\u9759\u7a33')  # 静稳 -> 静穏
src = src[:j] + fixed + src[k:]
bad3 = '\u7d99\u7d9c'
print('bad3 count:', src.count(bad3))
src = src.replace('\u7a4d\u307f\u5897\u3057\u7d9c', '\u7a4d\u307f\u5897\u3057\u7d99\u7d9c')
open('query-cosientist.md', 'w', encoding='utf-8').write(src)
src2 = open('query-cosientist.md', encoding='utf-8').read()
j = src2.find('- 2026-09-05: falsify \u7b2c63\u56de')
k = src2.find('\n', j)
print(repr(src2[j:k]))
