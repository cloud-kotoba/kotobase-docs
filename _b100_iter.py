import io

s = open('query-cosientist.md', encoding='utf-8').read()
lines = s.split('\n')

entry = (u"- 2026-09-06: bench \u7b2c100\u56de\u300221:26 JST tick\u3002worktree detached HEAD \u306e\u305f\u3081 "
         u"fetch + rev-parse \u6bd4\u8f03\u3067\u53d6\u308a\u8fbc\u307f (HEAD db5ee63 = falsify \u7b2c112\u56de run247 "
         u"\u307e\u3067\u53d6\u8fbc\u6e08\u307f\u78ba\u8a8d, \u602a\u96e2 0\u3002\u305f\u3060\u3057\u672c tick \u306f \u79fb\u52d5\u9078\u629e\u80a2\u3067\u8a08\u6e2c\u7d50\u679c\u3092\u8ffd\u8a18\u3002"
         u"falsify \u7b2c112\u56de hit \u306e\u6700\u65b0 NEXT\u306f\u300cK-Z3 21\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u884c\u300d\u3002"
         u"pre-run monitor \u306e NEXT\u300c23\u6642\u53f0\u300d\u306f stale \u3068\u5224\u65ad (rank \u7b2c90\u56de\u5e2f\u306e\u53e4\u3044\u30b9\u30ca\u30c3\u30d7\u30b7\u30e7\u30c3\u30c8, "
         u"rank \u7b2c105/108\u56de\u3067\u3082\u540c\u69d8\u306b\u5171\u6709\u5224\u65ad\u6e08\u307f\u3002)\u3002"
         u"live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002host load1 33.69\u219240.66 (21:26 uptime \u5b9f\u6e2c, "
         u"gate 7.5 \u5927\u5e45\u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057\u300chost busy (load1 33.69)\u300d\u3092\u8a18\u9332\u3057 "
         u"production HTTP \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (gate \u5916)\u3067 K-Z3 21\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run248A\u2013C \u3092\u5b9f\u65bd "
         u"(\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, 21:26:09\u201321:26:40 JST, "
         u"\u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test): "
         u"cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) \u2014 run248A \u5358\u767a 2.236s (6\u756a\u76ee) p50 83.0ms / "
         u"run248B \u5358\u767a 1.101s (5\u756a\u76ee) p50 74.3ms / run248C 0/20 p50 72.2ms, "
         u"control (kotobase.net/signup) cold 0/20 p50 72.4ms max 330.5ms \u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001"
         u"cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002run248A/B \u5358\u767a\u306f C 0/20 \u3067\u5373\u6d88\u5931\u3057\u300c\u5e2f\u5185\u6563\u767a\u5358\u767a\u5373\u6d88\u5931\u300d\u30d1\u30bf\u30fc\u30f3\u7d9a\u884c \u2014 "
         u"21\u6642\u53f0\u901a\u7b97 (falsify run245 3/60 + bench run246 1/60 + falsify run247 1/60 + \u672c tick 2/60) "
         u"7/240 (~2.9%) \u4f4e\u4f4d\u5e2f\u30b5\u30f3\u30d7\u30eb\u7d9a\u304f, 9/4 21\u6642\u53f0 ~58% \u8a18\u9332\u306e\u975e\u518d\u73fe\u304c 4 \u30bb\u30c3\u30c8\u7d9a\u304d\u3067 traffic \u4f9d\u5b58\u8aac\u306e\u65b9\u5411\u652f\u6301\u7d9a (n=4 \u30bb\u30c3\u30c8, \u5e2f\u786e\u5b9a\u306f rank \u5224\u5b9a\u306b\u59d4\u306d\u308b)\u3002"
         u"status \u9077\u79fb\u306a\u3057 (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a (curl \u306e\u307f + \u7d71\u8a08 python \u30d5\u30a1\u30a4\u30eb)\u3002"
         u"NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057\u7d9a\u884c, \u6b21 run ID \u306f run249 \u4f7f\u7528)\u3002")

# insert after '## Iteration log' line
anchor = '## Iteration log'
idx = None
for i, l in enumerate(lines):
    if l.strip() == anchor:
        idx = i
        break
if idx is None:
    raise SystemExit('anchor not found')
lines.insert(idx + 1, entry)

s2 = '\n'.join(lines)
open('query-cosientist.md', 'w', encoding='utf-8').write(s2)
open('/tmp/b100_iter_done.txt', 'w').write('inserted at line %d' % (idx + 2))