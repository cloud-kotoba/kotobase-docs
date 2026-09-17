#!/usr/bin/env python3
import io, re
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()

# ---- Fix 1: fold paragraph ----
start_marker = "\u7b2c115-120\u56de\u306e 24\u6642\u53f0(0\u6642\u53f0) folds:"
i = txt.find(start_marker)
if i < 0:
    raise SystemExit("fold start not found")
# paragraph ends at "\n\n(\n\n( K-Q2" boundary. Find next blank-line+newline then "( K-Q2"
j = txt.find("\n\n( K-Q2", i)
if j < 0:
    raise SystemExit("fold end not found")

new_fold = (
"\u7b2c115-120\u56de\u306e 24\u6642\u53f0(0\u6642\u53f0) folds: falsify \u7b2c122\u56de run268A-C (9/7 00:00, 24\u6642\u53f0\u5e2f\u521d\u8a08\u6e2c, cold 2/60 ~3.3% \u2014 run268A \u4e2d\u76e4\u96a3\u63a5\u30da\u30a2 2/20 1.757s/1.353s, B/C 0/20 \u5373\u6d88\u5931, control \u9759\u7a4f\u3067\u5206\u96e2\u6210\u7acb) + bench \u7b2c109\u56de run269A-C (00:07, cold 3/60 ~5.0% \u2014 run269A \u6563\u767a 3 \u4ef6 1.645/1.855/1.387s, B/C 0/20 \u5373\u6d88\u5931, control \u9759\u7a4f\u5206\u96e2\u6210\u7acb) + falsify \u7b2c123\u56de run270A-C (00:15, cold 1/60 ~1.7% \u2014 run270A \u5358\u767a 1.072s, B/C 0/20 \u5373\u6d88\u5931, control \u5b8c\u5168\u9759\u7a4f\u5206\u96e2\u6210\u7acb) + falsify \u7b2c124\u56de run271A-C (00:31, cold 7/60 ~11.7% \u2014 run271A heavy \u6563\u767a\u30af\u30e9\u30b9\u30bf 6/20 0.938-1.871s \u6563\u767a\u914d\u7f6e, run271B \u5358\u767a 1.202s, C 0/20, control cold 0/20 \u5b8c\u5168\u9759\u7a4f\u3067\u5206\u96e2\u6210\u7acb) + bench \u7b2c110\u56de run272A-C (00:39, cold 2/60 ~3.3% \u2014 run272A \u6563\u767a 2/20 1.16/1.43s, B/C 0/20 \u5373\u6d88\u5931, control cold 0/20 p50 0.042s \u5b8c\u5168\u9759\u7a4f\u3067\u5206\u96e2\u6210\u7acb) + cosientist \u7b2c117\u56de run273A-C (00:4x, cold 1/60 ~1.7% \u2014 run273A \u5358\u767a 1.103s \u6563\u767a, B/C 0/20 + control 0/20 \u5373\u6d88\u5931, control \u5b8c\u5168\u9759\u7a4f\u5206\u96e2\u6210\u7acb) + bench \u7b2c111\u56de run274A-C (cold 2/60 ~3.3% \u2014 run274A/274B \u5358\u767a 1.439s/1.119s, C 0/20 + control 0/20 \u5373\u6d88\u5931, control \u5b8c\u5168\u9759\u7a4f\u5206\u96e2\u6210\u7acb) \u3092\u53d6\u8fbc\u300124\u6642\u53f0\u901a\u7b97 = run268 (2/60) + run269 (3/60) + run270 (1/60) + run271 (7/60) + run272 (2/60) + run273 (1/60) + run274 (2/60) = 18/420 (~4.3%) \u306e 7 \u30bb\u30c3\u30c8\u9023\u7d9a cold>0\u3002\u6df1\u591c\u5e2f 24/0\u6642\u53f0 (traffic \u6700\u4f4e\u5e2f) \u3067\u5e2f\u521d\u304b\u3089 7 \u30bb\u30c3\u30c8\u9023\u7d9a cold>0 (2/60 \u2192 3/60 \u2192 1/60 \u2192 7/60 \u2192 2/60 \u2192 1/60 \u2192 2/60 \u306e\u6563\u767a\u6e1b\u5f31 \u2192 heavy \u518d\u4e0a\u632f\u308c \u2192 \u6563\u767a\u6e1b\u5f31\u3078\u306e\u632f\u5e45) \u304c\u51fa\u73fe\u3057\u3001run271A heavy 6/20 (run260A 8/20 / run263A 5/20 / run267A 5/20 \u578b) \u306e\u518d\u4e0a\u632f\u308c\u3092\u542b\u3080\u6df1\u591c\u5e2f\u3067\u306e cold \u9023\u7d9a\u51fa\u73fe\u306f K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d9a\u884c (\u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u65b9\u5411)\u3002\u305f\u3060\u3057\u5168\u30bb\u30c3\u30c8\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u578b (B/C 0/20 + control \u5206\u96e2\u6210\u7acb) \u3067 heavy \u306f\u5358\u4e00\u7a93\u5373\u6d88\u5931\u306e\u305f\u3081\u5e2f\u6c34\u6e96\u78ba\u5b9a\u30fb\u6a5f\u69cb\u5224\u65ad\u306b\u306f\u672a\u9054 (\u8ffd\u52a0 n \u7d99\u7d9a\u3001fallback \u5c02\u9580\u306e\u307e\u307e)\u3002status: K-Z3 open \u7d99\u7d9a (\u6c7a\u5b9a\u7684\u53cd\u8a3c/\u652f\u6301\u306b\u672a\u9054 \u2014 24\u6642\u53f0 18/420 ~4.3% \u306f 23\u6642\u53f0 ~5.6% \u3068\u540c\u6c34\u6e96\u306e\u4f4e\u301c\u4e2d\u4f4d\u5e2f\u5019\u88dc\u3067\u5e2f\u6c34\u6e96\u78ba\u5b9a\u306b\u81f3\u3089\u305a)\u3002"
)
txt = txt[:i] + new_fold + txt[j:]

with io.open(path,"w",encoding="utf-8") as f:
    f.write(txt)
print("fold corrected")