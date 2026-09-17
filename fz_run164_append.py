import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

anchor = "| K-Z3 | worker | K-Z1/K-Z2"
idx = text.index(anchor)
ev = (
    "falsify 2026-09-05 (K-Z3 19\u6642\u53f0 n \u7a4d\u307f\u589e\u3057 run164A\u2013C, "
    "run162 \u76f4\u5f8c\u306e\u8ffd\u52a0 n, \u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, "
    "\u5225\u63a5\u7d9a curl, Tokyo, 19:30:12\u201319:30:27 JST, \u5168 80/80 200, "
    "host load1 30.26 \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): "
    "run164A cold(>=0.5s) 0/20 p50 0.053s (max 0.184s) / run164B cold 0/20 p50 0.056s (max 0.145s) / "
    "run164C cold 0/20 p50 0.092s (max 0.137s) \u2014 landing control (kotobase.net/, \u540c\u6642\u523b, n=20, \u5168 200) "
    "\u306f cold 0/20 p50 0.088s (max 0.152s) \u3068\u9759\u7a33\u3067 control \u5206\u96e2\u6210\u7acb\u3002"
    "run162 \u578b\u306e landing \u5074\u9006\u8ee2\u6563\u767a\u3082\u975e\u518d\u73fe\u3067 3 run + control \u306e\u5168 80 \u8a66\u884c\u5b8c\u5168\u9759\u7a33\u3002"
    "19\u6642\u53f0\u901a\u7b97\u306f 2026-09-04 run88 (0/60) + run162 (0/60) + \u672c tick (0/60) \u3067 "
    "180 \u8a66\u884c\u4e2d 0 \u8a66\u884c\u306e\u4f4e\u4f4d\u5e2f (18\u6642\u53f0 ~0.8\u20132.2% \u3068\u540c\u7387\u5e2f)\u3002"
    "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002 "
)

text = text[:idx] + ev + text[idx:]
with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("inserted at", idx)
