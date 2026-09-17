# -*- coding: utf-8 -*-
import sys

PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
data = open(PATH, encoding='utf-8').read()
lines = data.split('\n')

# locate K-Z3 evidence cell (line starting with '| K-Z3 | worker |')
idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |') and '| worker |' in ln:
        idx = i
        break
assert idx is not None, "K-Z3 row not found"

# Anchor: current tail must end with the run305 fold sentence.
tail = lines[idx][-160:]
assert 'deep-night' in tail or '深夜最低帯' in tail, tail[-160:]

ADD = (" falsify 2026-09-07 (第140回, K-Z3 4hr(deep-night) n-add run306A\u2013C \u2014 "
"bench 第126回/cosientist 第120回 の run305 ID 衝突両採用に続く 4hr n-add (次 run ID run306), "
"\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 04:49\u201304:50 JST, "
"\u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test, "
"host load1 41.7\u201343.3 (uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, "
"secret \u4e0d\u542b \u2014 curl \u306e\u307f): "
"cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) \u2014 "
"run306A \u5358\u767a\u6563\u767a 1.4346s (idx9) p50 41.5ms max 1.435s / "
"run306B cold 0/20 p50 43.9ms max 101.7ms / run306C cold 0/20 p50 44.4ms max 64.8ms, "
"control (kotobase.net/signup) cold 0/20 p50 46.4ms max 116.0ms \u5b8c\u5168\u9759\u7a4f\u3067 "
"control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002"
"run306A \u5358\u767a\u306f B/C + control 0/20 \u3067\u5373\u6d88\u5931\u3057\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u6563\u767a\u5358\u767a\u578b\u7d99\u7d9a "
"(heavy \u30af\u30e9\u30b9\u30bf\u306f run271A 6/20 \u4ee5\u964d 31 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe)\u3002"
"4hr \u901a\u7b97 (run300 1/60 + run301 1/60 + run303 0/60 + run304 1/60 + "
"\u4e21 run305 2/60 + \u672c tick 1/60) = 6/360 (~1.7%) \u306e 6 \u30bb\u30c3\u30c8\u3001"
"deep-night \u7d2f\u8a08 run275..306 = 35/1860 (~1.9%) \u306e 31 \u30bb\u30c3\u30c8\u3067\u4f4e\u4f4d\u5e2f\u6c34\u6e96\u7d99\u7d9a "
"\u2014 \u6df1\u591c\u6700\u4f4e\u5e2f (traffic \u6700\u4f4e) 4\u6642\u53f0\u3067\u306e cold \u6563\u767a\u518d\u51fa\u73fe\u306f "
"K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d9a\u884c "
"(\u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u65b9\u5411)\u3002"
"status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002")

lines[idx] = lines[idx] + ADD
open(PATH, 'w', encoding='utf-8').write('\n'.join(lines))
print('APPENDED to line', idx+1, 'new_len', len(lines[idx]))