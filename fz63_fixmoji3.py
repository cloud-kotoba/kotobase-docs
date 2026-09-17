src = open('query-cosientist.md', encoding='utf-8').read()
pairs = [
    ('\u7b2c63\u56de\u3002rank NEXT\u300c\u59d4\u306d\u308b\u300d\u306e\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (K-Z3 \u73b0', 'X'),  # no-op placeholder
]
# targeted replacements in our log entry only
src = src.replace('\u73b0\u5728\u6642\u523b\u5e26 n \u7a4d\u307f\u5897\u3057) \u3092\u53d7\u3051\u3001', '\u73fe\u5728\u6642\u523b\u5e26 n \u7a4d\u307f\u5897\u3057) \u3092\u53d7\u3051\u3001')
src = src.replace('\u5b8c\u5168\u9759\u7a33\u3060\u304c', '\u5b8c\u5168\u9759\u7a33\u3060\u304c')  # check form
open('query-cosientist.md', 'w', encoding='utf-8').write(src)
src2 = open('query-cosientist.md', encoding='utf-8').read()
print('moji1 remaining:', src2.count('\u73b0\u5728\u6642\u523b\u5e26'))
# find mojibake candidates in our log line
j = src2.find('- 2026-09-05: falsify \u7b2c63\u56de')
print(repr(src2[j:j+260]))
