src = open('query-cosientist.md', encoding='utf-8').read()
bad = ['\u7b2c63\u56de\u3002rank NEXT\u300c\u59d4\u306d\u308b\u300d\u306e\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (K-Z3 \u73b0', '\u7a4d\u307f\u5897\u3057\u7d9c']
print('present before fix:', bad[0] in src)
src = src.replace('\u7b2c63\u56de\u3002rank NEXT\u300c\u59d4\u306d\u308b\u300d\u306e\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (K-Z3 \u7b2c', 'X')
src = src.replace('\u7a4d\u307f\u5897\u3057\u7d9c', '\u7a4d\u307f\u5897\u3057\u7d99\u7d9c')
open('query-cosientist.md', 'w', encoding='utf-8').write(src)
src2 = open('query-cosientist.md', encoding='utf-8').read()
print('partial-separated fix done:', '\u7a4d\u307f\u5897\u3057\u7d9c' not in src2)
