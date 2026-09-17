import sys

PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
data = open(PATH, encoding='utf-8').read()
lines = data.split('\n')

ANCHOR = 'run276A\u2013C \u2014 falsify \u7b2c125\u56de run275 (1\u6642\u53f0\u5e2f\u521d\u8a08\u6e2c) \u306b\u7d9a\u304f n \u7a4d\u307f\u5897\u3057'
assert ANCHOR in data, "anchor run276 line not found"

INS = (" falsify 2026-09-07 (\u7b2c126\u56de, K-Z3 1\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run277A\u2013C \u2014 "
"rank \u7b2c122\u56de NEXT\u300cK-Z3 1\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a (\u6b21 run ID \u306f run277 \u4f7f\u7528)\u300d\u306e run277 \u67a0\u3068\u3057\u3066\u5b9f\u65bd, "
"\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 01:16\u201301:19 JST, \u5168 80/80 200, "
"\u6b63 endpoint search.kotobase.net/search?q=test, host load1 47\u201363 (uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, "
"secret \u4e0d\u542b \u2014 curl \u306e\u307f): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) \u2014 "
"run277A cold 2/20 (1.0061s 1\u756a\u76ee / 1.4764s 10\u756a\u76ee \u2014 \u6563\u767a\u914d\u7f6e, warm \u7fa4 0.05\u20130.18s \u3067 cold \u3068\u4ea4\u4e92) p50 78.2ms max 1.476s / "
"run277B cold 0/20 p50 69.7ms max 300.8ms / run277C cold 0/20 p50 77.7ms max 221.0ms, "
"control (kotobase.net/signup) cold 0/20 p50 119.2ms max 257.5ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002"
"run277A cold 2/20 \u306f B/C 0/20 + control 0/20 \u3067\u5373\u6d88\u5931\u3057\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u6563\u767a\u5358\u767a/\u30da\u30a2\u578b\u7d99\u7d9a "
"(run275A 2/20 \u2192 run276A 2/20 \u2192 \u672c tick 2/20 \u306e\u6563\u767a\u30da\u30a2\u9023\u7d9a, heavy \u30af\u30e9\u30b9\u30bf\u306e\u518d\u73fe\u306a\u3057)\u3002"
"1\u6642\u53f0\u901a\u7b97 (falsify run275 2/60 + bench run276 2/60 + \u672c tick 2/60) = 6/180 (~3.3%) \u3067 24\u6642\u53f0 (18/420 ~4.3%) \u3068\u540c\u6c34\u6e96\u306e\u4f4e\u301c\u4e2d\u4f4d\u5e2f\u5019\u88dc \u2014 "
"\u6df1\u591c\u5e2f 1\u6642\u53f0 (traffic \u6700\u4f4e\u5e2f) \u3067\u306e cold \u9023\u7d9a\u51fa\u73fe\u306f K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d99\u7d9a "
"(\u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u65b9\u5411)\u3002\u305f\u3060\u3057\u5e2f n=3 \u30bb\u30c3\u30c8\u3067\u5e2f\u6c34\u6e96\u78ba\u5b9a\u30fb\u6a5f\u69cb\u5224\u65ad\u306b\u306f rank \u8ffd\u52a0 n \u3092\u8981\u3059\u308b\u3002"
"status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002")

out = []
inserted = False
for ln in lines:
    out.append(ln)
    if (not inserted) and ('falsify \u7b2c125\u56de run275 (1\u6642\u53f0\u5e2f\u521d\u8a08\u6e2c)' in ln and 'run276A' in ln):
        out.append(INS)
        inserted = True

assert inserted, "insertion point not applied"
open(PATH, 'w', encoding='utf-8').write('\n'.join(out))
print('INSERTED at line after run276 entry; run277 paragraph added once')