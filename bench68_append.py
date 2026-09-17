import re, io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

evidence = (
    " falsify 2026-09-06 (K-Z3 5\u6642\u53f0 1\u30bb\u30c3\u30c8\u76ee run185A\u2013C, \u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, "
    "\u5225\u63a5\u7d9a curl, Tokyo, 04:37 JST, \u5168 80/80 200, host load1 75.91 \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): "
    "run185A cold(>=0.5s) 0/20 p50 34ms (max 75ms) / run185B cold 0/20 p50 33ms (max 41ms) / run185C cold 0/20 p50 35ms (max 49ms) \u2014 "
    "landing control (kotobase.net/, \u540c\u6642\u523b, n=20, \u5168 200) \u306f cold 0/20 p50 42ms (max 50ms) \u3068\u9759\u7a33\u3067 control \u5206\u96e2\u6210\u7acb\u3002"
    "\u5168 3 run \u5b8c\u5168\u9759\u7a33 \u2014 5\u6642\u53f0\u306f\u65e2\u77e5\u306e\u6df1\u591c\u5e2f\u4f4e\u4f4d\u5e2f (~0-13%) \u3068\u6574\u5408\u3002"
    "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
)

# append to K-Z3 hypothesis row (before next line starting with "| K-")
lines = text.split("\n")
out = []
inserted = False
for i, ln in enumerate(lines):
    if not inserted and ln.startswith("| K-Z3 |"):
        out.append(ln + evidence)
        inserted = True
    else:
        out.append(ln)
if not inserted:
    raise SystemExit("K-Z3 row not found")
text2 = "\n".join(out)

# iteration log entry at end (after last line)
logentry = (
    "- 2026-09-06: falsify \u7b2c68\u56de\u300204:36 JST tick\u3002HEAD dac503b = fetch \u5f8c net-kotobase/main \u5148\u7aef\u4e00\u81f4\u3002"
    "host load1 75.91 (gate 7.5 \u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3002"
    "\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (bench \u7b2c67\u56de NEXT \u8a18\u8f09, production HTTP \u5b9f\u6e2c\u306f gate \u5916): "
    "K-Z3 5\u6642\u53f0 1\u30bb\u30c3\u30c8\u76ee run185A\u2013C (\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, 04:37 JST, \u5168 80/80 200): "
    "cold 0/0/0 per 20 = 0/60 \u5b8c\u5168\u9759\u7a33, warm \u7fa4 p50 33\u201335ms, control cold 0/20 p50 42ms \u9759\u7a33\u3067 control \u5206\u96e2\u6210\u7acb \u2014 "
    "5\u6642\u53f0\u521d\u8a08\u6e2c\u306f\u4f4e\u4f4d\u5e2f (\u5e2f\u767a\u73fe\u7387 ~0-13% \u306e\u4e0b\u9650\u5074)\u3002status \u9077\u79fb\u306a\u3057 (rank \u5c02\u9580)\u3002"
    "\u672c tick \u306f terminal foreground \u51fa\u529b\u304c\u7a7a\u3067\u623b\u308b\u969c\u5bb3\u306e\u305f\u3081 background \u5b9f\u884c + \u30d5\u30a1\u30a4\u30eb\u66f8\u304d\u51fa\u3057\u3067\u56de\u907f "
    "(cwd \u7d4c\u7531\u3067\u306f output \u30d5\u30a1\u30a4\u30eb\u304c\u6d88\u5931\u3057\u305f\u305f\u3081\u7d75\u5bfe\u30d1\u30b9\u6307\u5b9a\u306b\u5909\u66f4)\u3002"
    "secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u9375\u306f zero-fill\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 5\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a)\u3002"
)
if not text2.endswith("\n"):
    text2 += "\n"
text2 += logentry + "\n"

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text2)
print("OK inserted=%s len=%d" % (inserted, len(text2)))
