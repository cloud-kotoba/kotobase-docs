#!/usr/bin/env python3
# Append run401 evidence to END of K-Z3 row (L279). Scrub zero-width chars + verify.
path='query-cosientist.md'
ADDS=(" falsify 2026-09-07 (K-Z3 22\u6642\u53f0(9/7)\u5e2f\u8a08\u6e2c run401A\u2013C \u2014 bench181-run400 (21hr, cold 7/60) \u306b\u7d9a\u304f 22\u6642\u53f0\u5e2f\u65b0\u8a08\u6e2c, "
"\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, cold(>=0.5s), nearest-rank p50, \u6b63 endpoint search.kotobase.net/search?q=test, "
"22:09:18\u201322:09:39 JST, \u5168 80/80 200, host load1 32.72 (gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, "
"secret \u4e0d\u542b \u2014 curl \u306e\u307f): cold(>=0.5s) 7/1/0 per 20 = 8/60 (~13.3%) \u2014 run401A cold 7/20 heavy \u30af\u30e9\u30b9\u30bf "
"(2.6340/1.2098/2.2475/1.1682/1.4097/1.5324/1.1648s \u6563\u767a\u914d\u7f6e) p50 63.4ms max 2633.7ms / "
"run401B cold \u5358\u767a 1/20 (1.7696s) p50 61.0ms max 1769.6ms / run401C cold 0/20 p50 59.7ms max 204.5ms, "
"control (kotobase.net/signup) cold 1/20 (0.6542s) p50 51.6ms max 654.2ms \u2014 control \u5883\u754c 1 \u4ef6 (0.654s) \u3067\u5b8c\u5168\u9759\u798f\u4e0d\u6210\u7acb "
"borderline not-separated \u6ce8\u8a18 (search cold 7 \u4ef6 1.165\u20132.634s deep \u3068 control \u5883\u754c 0.654s \u306e\u9006\u65b9\u5411 "
"magnitude \u5206\u96e2\u5f31\u6210\u7acb, cold \u7fa4 search \u5074\u5c40\u5728). run401A cold 7/20 \u306f heavy (>=6/20) \u95d8\u5024\u518d\u9054\u5019\u88dc "
"(run400 21hr 7/60 \u306e\u5f8c 22\u6642\u53f0\u5e2f\u65b0 1 \u7a93\u76ee\u3067\u306e heavy \u4e0a\u632f\u308c) \u2014 B/C 0/40 \u5373\u6d88\u5931\u3067\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d"
" \u6563\u767a\u30af\u30e9\u30b9\u30bf\u578b\u7d9a\u3092\u4fdd\u6301 (heavy>=6/20 \u306e\u5e2f\u6c34\u6e96\u6301\u7d9a\u6027\u306f\u5e2f\u5185\u8ffd\u52a0 n \u3067\u78ba\u8a8d). "
"22\u6642\u53f0 (9/7) \u5e2f\u65b0\u8a08\u6e2c cold 8/60 (~13.3%) \u306e\u9ad8\u4f4d\u5e2f\u521d\u671f\u30b5\u30f3\u30d7\u30eb \u2014 21\u6642\u53f0 (19/300 ~6.3%) \u30fb20\u6642\u53f0 (20/360 ~5.6%) "
"\u3088\u308a\u9ad8\u4f4d\u3067\u591c\u5e2f traffic \u9077\u79fb\u8aac\u306e\u5f31\u3044\u652f\u6301\u65b9\u5411 (\u65e5\u4e2d\u5e2f traffic \u4f9d\u5b58\u8aac\u306e\u65b9\u5411\u652f\u6301\u7d9d\u7d9a, \u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u306e\u5bfe\u6bd4\u4e0d\u5909). "
"status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580). secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a.")
import re
ZW=re.compile('[\u200b-\u200f\u202a-\u202e\u2060\ufeff]')
ADDS=ZW.sub('',ADDS)
assert '#####' not in ADDS, 'has #####'
lines=open(path,encoding='utf-8').read().split('\n')
idx=278
was=len(lines[idx])
assert 'run401' not in lines[idx], 'run401 already present - abort'
lines[idx]=lines[idx]+ADDS
open(path,'w',encoding='utf-8').write('\n'.join(lines))
print(f"appended {len(ADDS)} chars; L279 grew {was}->{len(lines[idx])}; occurrence check:")
print("run401 count:", lines[idx].count('run401'))