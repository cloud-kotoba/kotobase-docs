import io

P = 'query-cosientist.md'
t = io.open(P, encoding='utf-8').read()
anchor = '## Iteration log\n- 2026-09-13: falsify \u7b2c257\u56de'
assert t.count(anchor) == 1, 'anchor not unique: %d' % t.count(anchor)

entry = (
    "- 2026-09-13: rank \u7b2c265\u56de (19:10 JST tick\u3002HEAD 39f0d37 = fetch \u5f8c bench_fetch/main \u5148\u7aef\u4e00\u81f4 (detached HEAD; fetch + rev-parse \u6bd4\u8f03, \u4e56\u96e3 0; git pull --ff-only \u4e0d\u4f7f\u7528\u624b\u9806\u3002monitor: host load1 8.20\u3002live smoke 200/200 (/ /signup)\u3002) rank \u7b2c264\u56de\u4ee5\u964d\u306e\u65b0\u898f\u78ba\u5b9a evidence \u306f 2 \u672c: (1) falsify \u7b2c257\u56de run595A-C (11:24 9/13): K-Z3 11\u6642\u53f0 (9/13) cold 1/60 (~1.7%), control \u5b8c\u5168\u9759\u7a33\u5206\u96e2\u6210\u7acb\u300211\u6642\u53f0 (9/13) \u901a\u7b97 14/240 (~5.8%) \u4f4e\u4f4d\u5e2f \u2014 K-Z4 \u65e5\u5dee\u4e88\u5b9a (9/9 ~1.7% / 9/10 ~16.7% / 9/11 ~8.3% / 9/13 ~5.8%) \u306e 4 \u65e5\u76ee\u304c\u4f4e\u4f4d\u5074\u306b\u5fa9\u5e30\u3057\u3001\u65e5\u5dee\u6210\u5206\u4eee\u8aac\u3068\u5f37\u6574\u5408 (9/10 \u306e ~16.7% \u306f\u5916\u308c\u5024\u7684\u3067\u306f\u306a\u304f\u65e5\u6b21\u690d\u3002\u305f\u3060\u3057 9/13 \u6642\u5e26\u5168\u4f53\u306e\u5e2f\u5185\u4ed6\u30bb\u30c3\u30c8\u306a\u3057\u3067\u30b5\u30f3\u30d7\u30ea\u30f3\u30b0 1 \u7a97\u306e\u53ef\u80fd\u6027\u6b8b\u5b58)\u3002(2) bench 05:07 tick run594 \u7121\u52b9 (/search 404 60/60, \u6570\u5024\u8a18\u9332\u306a\u3057) \u2014 /search 404 transient \u518d\u767a (4/4 tick \u4e2d 3 \u56de\u76ee) \u3002rank \u5224\u5b9a: (a) K-Z3/K-Z4 \u3068\u3082 status \u9077\u79fb\u306a\u3057 (K-Z4 \u306f\u540c\u5e2f\u9023\u7d9a 2 \u65e5 \u30da\u30a2\u8981\u4ef6\u306e\u305f\u3081 19\u6642\u53f0 3 \u65e5\u76ee\u306e\u78ba\u5b9a\u5f85\u3061\u3002\u5b9f\u6e2c\u6570\u5b57\u306e\u307f\u3067\u5224\u5b9a\u3059\u308b)\u3002K-Z4 \u306e\u671f\u5f85 gain \u3092\u4e0a\u3052\u3066 top NEXT \u306b\u6307\u5b9a: 19\u6642\u53f0\u306f 9/11 run584 11/60 (~18.3%) vs 9/12 17/180 (~9.4%) \u306e 2 \u65e5\u5206\u5df2\u6e2c\u3002\u672c tick \u304c 19\u6642\u53f0 9/13 \u3067\u3042\u308a\u3001\u540c\u5e2f 3 \u65e5\u9023\u7d9a\u306e\u30da\u30a2\u6e2c\u5b9a\u306b\u3088\u308a K-Z4 \u65e5\u5dee\u6210\u5206\u306e\u5e2f\u56fa\u6709\u6c34\u6e96\u304b\u3089\u306e\u5206\u96e2\u3092\u76f4\u63a5\u5224\u5b9a\u3067\u304d\u308b\u6700\u3082\u60c5\u5831\u91cf\u306e\u9ad8\u3044 1 \u30bb\u30c3\u30c8\u3002(5) /search 404 \u5bfe\u7b56\u7dad\u6301: \u5b9f\u6e2c\u524d 3 endpoint smoke \u3067 404 \u306a\u3089\u6570\u5024\u8a18\u9332\u305b\u305a\u7d42\u4e86\u3002NEXT: K-Z3 19\u6642\u53f0 (9/13) run596A-C (\u540c\u5e2f 3 \u65e5\u9023\u7d9a\u30da\u30a2\u3067 K-Z4 \u65e5\u5dee\u6210\u5206\u3092\u76f4\u63a5\u5224\u5b9a\u3002\u5b9f\u6e2c\u524d 3 endpoint smoke \u6700\u512a\u5148\u3002secret \u4e0d\u542b\u3002)"
)

t2 = t.replace(anchor, '## Iteration log\n' + entry + '\n- 2026-09-13: falsify \u7b2c257\u56de')
io.open(P, 'w', encoding='utf-8').write(t2)
c = t2.count('## Iteration log')
assert c == 1, c
assert t2.count('rank \u7b2c265\u56de (19:10') == 1
print('OK inserted, header count', c)
