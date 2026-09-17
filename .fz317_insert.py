import io

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(PATH, encoding="utf-8") as f:
    lines = f.read().split("\n")

# locate "## Iteration log" header (0-based index)
H = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        H = i
        break
assert H is not None, "Iteration log header not found"

# sanity: last K-Z3 evidence line is directly above the header
assert lines[H-1].startswith(" rank 第138回"), f"expected K-Z3 fold line above, got: {lines[H-1][:60]}"
# sanity: newest iter-log entry is directly below the header
assert lines[H+1].startswith("- 2026-09-07: bench 第131回"), f"expected bench131 below, got: {lines[H+1][:60]}"

EV = (
    " falsify 2026-09-07 (第146回, K-Z3 6時台(深夜帯\u2192朝の帯境) n \u7a4d\u307f\u5897\u3057 run317A\u2013C \u2014 bench \u7b2c131\u56de (06:12, run316) \u306b\u7d9a\u304f 6\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 (\u6b21 run ID run317), "
    "\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 06:16\u201306:17 JST, \u5168 80/80 200, "
    "\u6b63 endpoint search.kotobase.net/search?q=test, host load1 44.68\u219251.56 (06:15/06:16 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, "
    "secret \u4e0d\u542b \u2014 curl \u306e\u307f): cold(>=0.5s) 0/0/0 per 20 = 0/60 \u5b8c\u5168\u9759\u7a4f \u2014 "
    "run317A cold 0/20 p50 46.6ms max 184.2ms / run317B cold 0/20 p50 94.8ms max 176.4ms / run317C cold 0/20 p50 65.1ms max 210.2ms, "
    "control (kotobase.net/signup) cold 0/20 p50 127.1ms max 390.8ms \u9759\u7a4f (threshold \u8d85\u3048\u305a, host load \u9ad8\u9a30 tick \u306e p50 \u4e0a\u632f\u308c note, cold \u6fc3\u5ea6\u5224\u5b9a 0/60 \u306b\u5f71\u97ff\u306a\u3057) \u3067 control \u5206\u96e2\u6210\u7acb (search/control \u3068\u3082 0 cold)\u3002"
    "run317 \u5168 0/60 \u5b8c\u5168\u9759\u7a4f\u306f 6\u6642\u53f0\u306e\u5b8c\u5168\u9759\u7a4f 0/60 \u3067 run283/289/293/296/297/298/303/307/309/312/313/314 \u578b\u306e **13 \u4f8b\u76ee** "
    "(bench run316 \u5358\u767a 1/60 \u76f4\u5f8c\u306e\u9023\u7d9a\u518d\u9759\u7a4f, \u6563\u767a\u5358\u767a=\u5373\u6d88\u5931\u306e\u6027\u8cea\u3092 13 \u4f8b\u76ee\u3067\u652f\u6301, heavy run271A 6/20 \u578b\u306f run271A \u4ee5\u964d 42 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe)\u3002"
    "6\u6642\u53f0\u901a\u7b97 = falsify run315 (2/60) + bench run316 (1/60) + \u672c tick run317 (0/60) = 3/180 (~1.67%) \u306e 3 \u30bb\u30c3\u30c8\u3001"
    "deep-night \u7d2f\u8a08 run275..317 = 43/2580 (~1.67%) \u306e 43 \u30bb\u30c3\u30c8\u3067\u4f4e\u4f4d\u5e2f\u6c34\u6e96\u7d99\u7d9a \u2014 "
    "\u6df1\u591c\u5e2f\u2192\u671d\u306e\u5e2f\u5883 (6\u6642\u53f0) \u3067\u306e\u5b8c\u5168\u9759\u7a4f\u518d\u51fa\u73fe (run315 \u6563\u767a\u30da\u30a2 \u2192 run316 \u5358\u767a \u2192 \u672c tick 0/60 \u306e\u6563\u767a\u6e1b\u5f31\u2192\u9759\u7a4f) \u306f "
    "K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d9a\u884c (\u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u65b9\u5411, deep-night \u7d2f\u8a08 ~1.67% \u306e\u4f4e\u4f4d\u5e2f\u6b8b\u754c\u304c 43 \u30bb\u30c3\u30c8\u3067\u5b89\u5b9a)\u3002"
    "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002"
)

IL = (
    "- 2026-09-07: falsify \u7b2c146\u56de\u300206:16 JST tick\u3002HEAD 235cde2 = bench \u7b2c131\u56de (run316A-C, 06:12, 6\u6642\u53f0 n-add, cold 1/60) = remote net-kotobase/main \u4e00\u81f4 "
    "(fetch + rev-parse \u6bd4\u8f03, \u97da\u96e2 0; worktree detached HEAD \u306e\u305f\u3081 git pull --ff-only \u4e0d\u53ef, fetch \u7cfb\u3067\u53d6\u308a\u8fbc\u307f)\u3002"
    "live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002host load1 44.68\u219251.56 (06:15/06:16 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057 production HTTP \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (gate \u5916)\u3002"
    "rank \u7b2c139\u56de NEXT\u300cK-Z3 current-band(6\u6642\u53f0) n-add (run316)\u300d\u306e\u7d99\u7d9a\u67a0 (bench \u7b2c131\u56de run316 \u6e08\u307f) \u3068\u3057\u3066\u73fe\u6642\u523b\u5e2f 6\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run317A\u2013C \u3092\u5b9f\u65bd "
    "(\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 06:16\u201306:17 JST, \u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test): "
    "cold(>=0.5s) 0/0/0 per 20 = 0/60 \u5b8c\u5168\u9759\u7a4f \u2014 run317A 0/20 p50 46.6ms / run317B 0/20 p50 94.8ms / run317C 0/20 p50 65.1ms, "
    "control (kotobase.net/signup) 0/20 p50 127.1ms max 390.8ms \u9759\u7a4f (threshold \u8d85\u3048\u305a, host load \u9ad8\u9a30 p50 \u4e0a\u632f\u308c note, 0/60 \u5224\u5b9a\u306b\u5f71\u97ff\u306a\u3057)\u3002"
    "run317 \u5b8c\u5168\u9759\u7a4f 0/60 \u306f 13 \u4f8b\u76ee, bench run316 \u5358\u767a\u76f4\u5f8c\u306e\u9023\u7d9a\u518d\u9759\u7a4f, heavy run271A \u4ee5\u964d 42 \u30bb\u30c3\u30c8\u975e\u518d\u73fe\u3002"
    "6\u6642\u53f0\u901a\u7b97 (falsify run315 2/60 + bench run316 1/60 + \u672c tick 0/60) = 3/180 (~1.67%) 3-set\u3001"
    "deep-night \u7d2f\u8a08 run275..317 = 43/2580 (~1.67%) 43-set \u4f4e\u4f4d\u5e2f\u7d99\u7d9a \u2014 \u6df1\u591c\u5e2f\u2192\u671d\u306e\u5e2f\u5883\u3067\u306e\u5b8c\u5168\u9759\u7a4f\u518d\u51fa\u73fe\u306f K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d9a\u884c\u3002"
    "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a (curl \u306e\u307f + \u7d71\u8a08 python)\u3002"
    "NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 6\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u3001\u6b21 run ID \u306f run318 \u4f7f\u7528)\u3002"
)

# insert evidence line at H (before "## Iteration log"), then iter-log at H+2 (after header)
lines.insert(H, EV)
lines.insert(H+2, IL)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("INSERTED OK")
print("H =", H)