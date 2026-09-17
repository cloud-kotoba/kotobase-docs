import io

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(PATH, encoding="utf-8") as f:
    lines = f.read().split("\n")

H = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        H = i
        break
assert H is not None

# sanity on structure
assert lines[278].startswith("| K-Z3 |"), lines[278][:40]
assert lines[H-1].startswith(" rank 第138回") or "rank 第138回" in lines[H-1], lines[H-1][:60]
assert lines[H+1].startswith("- 2026-09-07: bench 第133回"), lines[H+1][:40]

EV = (
    " falsify 2026-09-07 (\u7b2c147\u56de, K-Z3 6\u6642\u53f0(\u6df1\u591c\u5e2f\u2192\u671d\u306e\u5e2f\u5883) independent n-add run319A\u2013C \u2014 "
    "bench \u7b2c133\u56de run319 (0/60 \u5b8c\u5168\u9759\u7a4f, 06:41) \u3068\u306f\u5225\u306e\u5358\u72ec\u8868\u63a2\u6784 (run ID \u884c\u7a81 i.e. run319 \u30b3\u30ea\u30b8\u30e7\u30f3, run314/run263/run216 \u5148\u4f8b\u306e\u72ec\u7acb 2 \u6e2c\u5b9a, \u672c\u6e2c 06:39), "
    "\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 06:39:0x JST, \u5168 80/80 200, "
    "\u6b63 endpoint search.kotobase.net/search?q=test, host load1 33.24 (06:30 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, "
    "secret \u4e0d\u542b \u2014 curl \u306e\u307f): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) \u2014 "
    "run319A cold 3/20 (0.8349s 13\u756a\u76ee / 0.9927s 1\u756a\u76ee / 1.3877s 2\u756a\u76ee \u2014 \u5192\u982d idx1-2 + \u4e2d\u76e4 idx13 \u306e\u6563\u767a\u914d\u7f6e, warm \u7fa4 0.035\u20130.281s \u3068\u4ea4\u4e92) p50 78.9ms "
    "/ run319B cold 0/20 p50 51.3ms max 185.9ms / run319C cold 0/20 p50 53.2ms max 223.6ms, "
    "control (kotobase.net/signup) cold 0/20 p50 77.6ms max 184.9ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002"
    "run319A cold 3/20 \u306f B/C 0/20 + control 0/20 \u3067\u5373\u6d88\u5931\u3057\u3001bench \u7b2c133\u56de\u306e\u540c run319 \u7a93 (0/60 \u5b8c\u5168\u9759\u7a4f) \u30682\u5206\u3046\u3061\u306e\u72ec\u7acb\u7a93\u3067\u5bfe\u7167\u3055\u308c\u3001"
    "run317-318-319 \u201c\u5b8c\u5168\u9759\u7a4f 3 \u9023\u7d9a\u201d \u8aad\u307f\u3092\u5272\u308b\u6563\u767a\u30af\u30e9\u30b9\u30bf\u518d\u51fa\u73fe \u2014 "
    "\u6df1\u591c\u5e2f traffic \u6700\u4f4e\u5e2f (6\u6642\u53f0) \u3067 cold \u30af\u30e9\u30b9\u30bf\u304c\u5b8c\u5168\u9759\u7a4f\u7a93\u8fd1\u5074\u306e\u72ec\u7acb\u7a93\u306b\u518d\u51fa\u73fe\u3057\u3001"
    "K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d9a\u884c (\u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u65b9\u5411\u3001\u6df1\u591c\u5e2f \u30af\u30e9\u30b9\u30bf/\u5358\u767a = 1\u7a93\u751f\u5373\u6d88\u5931\u306e\u6027\u8cea\u3092\u652f\u6301)\u3002"
    "6\u6642\u53f0\u901a\u7b97 (bench run319 0/60 \u8ffd\u8a18\u3057\u305f\u5751\u3067 run315 2/60 + run316 1/60 + run317 0/60 + run318 0/60) + \u672c tick \u72ec\u7acb run319 3/60 = 6/300 (~2.0%) \u3001"
    "heavy run271A 6/20 \u578b\u306f run271A \u4ee5\u964d 45 \u30bb\u30c3\u30c8\u975e\u518d\u73fe \u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002"
)

IL = (
    "- 2026-09-07: falsify \u7b2c147\u56de\u300206:39 JST\u3002HEAD 2a10d23 = rank \u7b2c141\u56de (run318+run319 fold, 06:49, 6\u6642\u53f0 n-add \u5b8c\u5168\u9759\u7a4f 2/\u305d\u306e NEXT run320) = remote net-kotobase/main \u4e00\u81f4 "
    "(fetch + rev-parse \u6bd4\u8f03, \u97da\u96e2 0; worktree detached HEAD \u306e\u305f\u3081 git pull --ff-only \u4e0d\u53ef, fetch \u7cfb\u3067\u53d6\u308a\u8fbc\u307f)\u3002"
    "live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002host load1 33.24 (06:30 uptime, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057 production HTTP \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (gate \u5916)\u3002"
    "rank \u7b2c141\u56de NEXT\u300cK-Z3 current-band(6\u6642\u53f0) n-add (run320)\u300d\u3001bench \u7b2c133\u56de\u304c run319 \u3092\u5148\u884c\u4f7f\u7528 (0/60 \u5b8c\u5168\u9759\u7a4f, 06:41)\u3002"
    "\u672c tick \u306f\u30b3\u30ea\u30b8\u30e7\u30f3\u7a93\u3068\u306a\u3063\u3066\u3044\u308b\u3082\u306e\u306e\u72ec\u7acb 2 \u6e2c\u5b9a\u3068\u3057\u3066 run319A\u2013C \u3092\u5b9f\u65bd (run314/run263/run216 \u5148\u4f8b\u306e\u72ec\u7acb\u81ea\u7acb\u6e2c\u5b9a, 06:39): "
    "cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) \u2014 run319A cold 3/20 (0.8349/0.9927/1.3877s, idx1-2+13 \u6563\u767a\u30af\u30e9\u30b9\u30bf) p50 78.9ms / run319B 0/20 / run319C 0/20, "
    "control 0/20 \u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4 search \u5c40\u5728\u3002"
    "bench \u7b2c133\u56de run319 (0/60 \u5b8c\u5168\u9759\u7a4f) \u30681\u7a93 2\u5206\u5dee\u306e\u72ec\u7acb\u7a93\u3067\u5bfe\u7167\u3055\u308c\u3001\u9031\u5dee\u3067\u306e\u6563\u767a\u30af\u30e9\u30b9\u30bf\u518d\u51fa\u73fe\u3067 \u201c\u5b8c\u5168\u9759\u7a4f 3 \u9023\u7d9a\u201d \u8aad\u307f\u3092\u5272\u308b \u2014 "
    "6\u6642\u53f0\u3067\u306e cold \u6563\u767a\u518d\u51fa\u73fe\u306f K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d9a\u884c (\u6df1\u591c\u5e2f\u2192\u671d\u306e\u5e2f\u5883\u3067\u306e\u5373\u6d88\u5931\u6563\u767a\u306e\u6027\u8cea\u3092\u652f\u6301, heavy run271A \u4ee5\u964d 45 \u30bb\u30c3\u30c8\u975e\u518d\u73fe)\u3002"
    "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a (curl \u306e\u307f + \u7d71\u8a08 python)\u3002"
    "NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 6\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u3001\u6b21 run ID \u306f run320 \u4f7f\u7528)\u3002"
)

# append evidence inline to K-Z3 row line (index 278) END per memory rule
lines[278] = lines[278] + EV

# insert iter-log entry right after header (newest-first)
lines.insert(H+1, IL)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("OK H=", H)