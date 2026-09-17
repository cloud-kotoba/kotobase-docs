import io

s = open('query-cosientist.md', encoding='utf-8').read()
lines = s.split('\n')

# Append bench 第100回 run248 evidence to K-Z3 row (line 243, idx 242)
ev = (u" bench 2026-09-06 (第100回, K-Z3 21時台 n 積み増し run248A\u2013C, "
      u"同測定法 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, "
      u"21:26:09\u201321:26:40 JST, \u5168 80/80 200, \u6b63 endpoint "
      u"search.kotobase.net/search?q=test, host load1 33.69\u219240.66 (21:26 uptime \u5b9f\u6e2c, "
      u"gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916 \u2014 "
      u"rank \u7b2c108\u56de NEXT\u300cK-Z3 21\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u300d\u306b\u5f93\u3044 "
      u"21\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run248A\u2013C \u3092\u5b9f\u65bd; pre-run monitor \u306e NEXT\u300c23\u6642\u53f0\u300d\u306f stale \u3068\u5224\u65ad): "
      u"cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) \u2014 run248A \u5358\u767a 2.236s (6\u756a\u76ee, \u7a81\u767a) "
      u"p50 83.0ms (warm \u7fa4 52\u2013194ms) / run248B \u5358\u767a 1.101s (5\u756a\u76ee) p50 74.3ms / "
      u"run248C 0/20 p50 72.2ms max 152.2ms, control (kotobase.net/signup) cold 0/20 p50 72.4ms "
      u"max 330.5ms \u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728 \u2014 "
      u"run248A 2.236s \u5358\u767a\u306f C 0/20 \u3067\u5373\u6d88\u5931\u3057\u300c\u5e2f\u5185\u6563\u767a\u5358\u767a\u5373\u6d88\u5931\u300d\u30d1\u30bf\u30fc\u30f3\u7d99\u7d9a \u2014 "
      u"21\u6642\u53f0\u901a\u7b97 (falsify run245 3/60 + bench run246 1/60 + falsify run247 1/60 + \u672c tick 2/60) "
      u"7/240 (~2.9%) \u4f4e\u4f4d\u5e2f\u30b5\u30f3\u30d7\u30eb\u7d9a\u304f (n=4 \u30bb\u30c3\u30c8), "
      u"9/4 21\u6642\u53f0 ~58% \u8a18\u9332\u3068\u306e 2 \u65e5\u5dee\u5bfe\u6bd4\u306f\u4f4e\u4f4d\u5074\u3067 traffic \u4f9d\u5b58\u8aac\u306e\u65b9\u5411\u652f\u6301\u7d9a\u3002"
      u"status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002")

if lines[242].endswith('status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002'):
    lines[242] = lines[242] + ev
else:
    # append at end regardless
    lines[242] = lines[242] + ev

s2 = '\n'.join(lines)
open('query-cosientist.md', 'w', encoding='utf-8').write(s2)
open('/tmp/b100_append_done.txt', 'w').write('appended LEN now %d' % len(lines[242]))