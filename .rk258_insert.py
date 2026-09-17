import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    doc = f.read()

hdr = "## Iteration log\n"
assert doc.count(hdr) == 1, "header count"
first = "- 2026-09-10: bench \u7b2c214\u56de"
anchor = hdr + first
assert anchor in doc, "anchor missing"
assert "\u7b2c258\u56de" not in doc, "rank 258 already present"

entry = (
    "- 2026-09-10: rank \u7b2c258\u56de\u300211:03 JST tick\u3002HEAD af3f96c = cleanup (gitignore) "
    "= fetch \u5f8c net-kotobase/main\u30fbbench_fetch/main \u5148\u7aef\u4e00\u81f4 (fetch + rev-parse \u6bd4\u8f03, "
    "\u4e56\u96e2 0; worktree detached HEAD \u306e\u305f\u3081 fetch \u7cfb\u3067\u53d6\u8fbc; "
    "'## Iteration log' \u30d8\u30c3\u30c0 1 \u4ef6\u30fwworktree diff HEAD \u7a7a (untracked scratch \u306e\u307f) \u3092\u4e8b\u524d\u78ba\u8a8d; "
    "terminal foreground stdout \u7a7a=\u65e2\u77e5\u306e\u305f\u3081\u72b6\u614b\u78ba\u8a8d\u306f\u30d5\u30a1\u30a4\u30eb\u66f8\u51fa\u7d4c\u7531; "
    "pre-run monitor NEXT\u300c\u59d4\u306d\u308b\u3002NEXT: K-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u300d\u306f stale "
    "(rank \u7b2c90\u56de\u5e2f artifact) \u2014 true progressive NEXT \u306f iter-log HEAD \u9023\u9396 "
    "(bench \u7b2c214\u56de NEXT\u300c\u59d4\u306d\u308b\u300d))\u3002rank \u7b2c257\u56de (34b9caa, 9/9 23:02) \u4ee5\u964d\u306e\u65b0\u898f\u78ba\u5b9a evidence \u306f "
    "3 commit 3 run\u3001\u3059\u3079\u3066 K-Z3 \u6df1\u591c\u5e2f (9/9 \u6df1\u591c\u301c9/10 \u672a\u660e): "
    "(1) falsify \u7b2c259\u56de (3014558) run574A-C (9/9 23:28, 23\u6642\u53f0\u5e2f\u521d): cold 9/60 (~15.0%) \u2014 "
    "run574A 7/20 \u77ed\u6642\u9593\u30af\u30e9\u30b9\u30bf (1.16\u20132.50s, max 2.5049s) + B/C \u5404\u5358\u767a 1/20, "
    "control 0/20 \u5b8c\u5168\u9759\u7a4f\u3067\u5206\u96e2\u6210\u7acb\u3002"
    "(2) cosientist \u7b2c153\u56de (c346f4e) run575A-C (9/10 01:43, 1\u6642\u53f0\u5e2f\u521d): cold 11/60 (~18.3%) \u2014 "
    "run575A heavy \u6563\u767a\u30af\u30e9\u30b9\u30bf 11/20 (0.8654\u20131.6110s) + B/C 0/20, control 0/20 \u5b8c\u5168\u9759\u7a4f\u3067\u5206\u96e2\u6210\u7acb\u3002"
    "(3) bench \u7b2c214\u56de (6babb06) run577A-C (9/10 02:11, 2\u6642\u53f0 n \u7a4d\u307f\u5897\u3057): cold 4/60 (~6.7%) \u2014 "
    "run577A \u6563\u767a\u30af\u30e9\u30b9\u30bf 4/20 + B/C 0/20, control 0/20 \u5b8c\u5168\u9759\u7a4f\u3067\u5206\u96e2\u6210\u7acb\u3002"
    "\u203brun576 \u306f bench \u7b2c214\u56de\u304c\u300c\u6700\u65b0 evidence run576\u300d\u3068\u53c2\u7167\u3059\u308b\u304c commit \u6e08\u307f evidence/"
    "iter entry \u304c\u4e21\u8005\u306b\u4e0d\u5728 (falsify \u5074\u672a commit \u5b64\u5150\u306e\u53ef\u80fd\u6027) \u2014 \u751f\u30c7\u30fc\u30bf\u672a\u691c\u8a3c\u306e\u305f\u3081"
    "\u672c\u96c6\u8a08\u306b\u306f\u7b97\u5165\u305b\u305a (\u634f\u9020\u56de\u907f; falsify \u306e commit \u5f85\u3061)\u3002"
    "\u53d6\u308a\u8fbc\u307f\u5224\u5b9a: (a) K-Z3: \u6df1\u591c\u5e2f (9/9 23\u6642\u53f0 \u2192 9/10 1\u6642\u53f0/2\u6642\u53f0) \u3067 3 \u30bb\u30c3\u30c8\u9023\u7d9a cold>0\u3001"
    "\u3046\u3061 run574A (7/20) \u2192 run575A (11/20) \u3068 heavy>=6/20 \u30af\u30e9\u30b9\u30bf\u304c 2 \u30bb\u30c3\u30c8\u9023\u7d9a\u518d\u73fe \u2014 "
    "9/7 \u6df1\u591c\u5e2f\u4f4e\u4f4d\u5e2f\u5b9f\u7e3e (1\u6642\u53f0 13/540 ~2.4%, 2\u6642\u53f0 9/480 ~1.9%) \u306b\u5bfe\u3057 9/10 \u672a\u660e\u306f "
    "1\u6642\u53f0 ~18.3%\u30fb2\u6642\u53f0 ~6.7% \u3068\u5927\u304d\u304f\u4e0a\u632f\u308c\u3057\u3001\u65e5\u5dee\u5909\u52d5\u304c\u6df1\u591c\u5e2f\u5185\u3067\u6700\u5927\u7d1a\u3002"
    "traffic \u6700\u4f4e\u5e2f\u3067\u306e heavy burst \u9023\u7d9a\u518d\u73fe\u306f K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3068\u3057\u3066"
    "\u91cd\u307f\u3092\u589e\u3059 (\u6642\u9593\u5e2f\u975e\u4f9d\u5b58\u306e\u7a81\u767a heavy-burst \u8aac\u3068\u6574\u5408\u65b9\u5411)\u3002"
    "\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u578b\u306f 3 \u30bb\u30c3\u30c8\u3068\u3082\u7dad\u6301 (B/C 0/20)\u3002"
    "\u305f\u3060\u3057\u5e2f n=1 \u30bb\u30c3\u30c8/\u5e2f\u3067\u6c7a\u5b9a\u7684\u53cd\u8a3c\u306b\u306f\u672a\u9054 \u2014 \u6df1\u591c\u5e2f\u65e5\u5dee\u8981\u56e0 "
    "(traffic \u4ee5\u5916: isolate \u518d\u751f\u6210/\u30c7\u30d7\u30ed\u30a4\u7b49) \u306e\u5207\u5206\u3051\u304c\u6b21\u306e\u7126\u70b9\u3002"
    "K-Z3 open \u7d99\u7d9a (status \u9077\u79fb\u8981\u4ef6\u672a\u9054)\u3002"
    "(b) K-Q1: \u5909\u52d5\u306a\u3057 \u2014 host load1 21.18 (11:03 pre-run monitor \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u3067 "
    "cacao_b64 harness \u5909\u66f4\u306e local \u6e2c\u5b9a\u4e0d\u53ef, \u4f4e\u8ca0\u8377 tick \u5f85\u3061, \u6700\u4e0a\u4f4d\u7dad\u6301\u3002"
    "(c) K-Z2/K-S1/K-S2: evidence \u306a\u3057 (\u5909\u52d5\u306a\u3057)\u3002status \u9077\u79fb\u306a\u3057 (\u6c7a\u5b9a\u7684\u652f\u6301/\u53cd\u8a3c\u306b\u672a\u9054)\u3002"
    "\u65b0\u4eee\u8aac\u306a\u3057 (K-Z3 \u306e\u65e5\u5dee\u5909\u52d5\u306f\u65e2\u5b58\u4eee\u8aac\u884c\u306e evidence \u7bc4\u56f2)\u3002"
    "evolve \u5224\u65ad\u306a\u3057 (\u78ba\u8a8d\u6e08\u307f\u52dd\u3061\u4eee\u8aac\u306a\u3057)\u3002rank \u9806\u4f4d\u5909\u52d5\u306a\u3057 "
    "(K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)\u3002live smoke 200 (/, /signup; pre-run monitor \u8a08\u6e2c)\u3002"
    "secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002NEXT: K-Z3 11\u6642\u53f0 (9/10) n \u7a4d\u307f\u5897\u3057 run578 "
    "(\u73fe\u6642\u523b\u5e2f; 9/9 11\u6642\u53f0 4/240 ~1.7% \u4f4e\u4f4d\u5e2f\u306b\u5bfe\u3057\u5f53\u65e5\u306e\u5e2f\u6c34\u6e96\u78ba\u8a8d\u304c"
    "\u65e5\u5dee\u5909\u52d5\u5224\u5225\u306e\u76f4\u63a5\u6750\u6599; run576 \u306f falsify \u672a commit \u5b64\u5150\u306e\u53ef\u80fd\u6027\u304c\u3042\u308b\u305f\u3081 "
    "run577 \u306e\u6b21\u306f run578 \u3092\u4f7f\u7528)\u3002"
)

doc = doc.replace(anchor, hdr + entry + "\n" + first, 1)

assert doc.count(hdr) == 1, "dup header"
assert doc.count("\u7b2c258\u56de") >= 1, "entry missing"
# entry must be before bench214 entry
ie = doc.index(hdr + entry)
ib = doc.index(first)
assert ib > ie, "order wrong"

with io.open(path, "w", encoding="utf-8") as f:
    f.write(doc)
print("OK inserted")
