#!/usr/bin/env python3
"""falsify 152: append K-Z3 run328 evidence to cell L279 END +
insert iter-log entry after '## Iteration log'. No -e/-c, no heredoc."""
import io

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ev = (" falsify 2026-09-07 (第152回, K-Z3 8時台帯初計測 run328A\u2013C \u2014 7時台 (run321\u2013327) \u306b\u7d9a\u304f 8\u6642\u53f0, "
      "\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 08:03:41 JST, \u5168 80/80 200, "
      "\u6b63 endpoint search.kotobase.net/search?q=test, host load1 83.69 (08:03 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) "
      "\u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) "
      "\u2014 run328A \u5358\u767a\u6563\u767a 1.084s (7\u756a\u76ee) p50 176.0ms / run328B cold 0/20 p50 139.1ms max 269.4ms "
      "/ run328C cold 0/20 p50 186.0ms max 405.5ms, control (kotobase.net/signup) cold 0/20 p50 146.5ms max 235.9ms "
      "\u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002run328A \u5358\u767a\u306f B/C 0/20 + control 0/20 "
      "\u3067\u5373\u6d88\u5931\u3057\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u6563\u767a\u5358\u767a\u578b\u7d99\u7d9a\u3001heavy \u30af\u30e9\u30b9\u30bf\u306f run271A \u4ee5\u964d 53 \u30bb\u30c3\u30c8\u975e\u518d\u73fe\u3002"
      "8\u6642\u53f0 (9/7) \u5e2f\u521d\u8a08\u6e2c cold 1/60 (~1.7%) \u306e\u4f4e\u4f4d\u5e2f\u5019\u88dc \u2014 host load \u9ad8\u9a30 (83) \u3067 p50 \u5168\u4f53\u7684\u4e0a\u632f\u308c "
      "(139\u2013186ms max 405.5ms) \u3060\u304c control 0/20 \u9759\u7a4f\u3067 cold \u95c7\u5024\u5224\u5b9a 1/60 \u306b\u5f71\u97ff\u306a\u3057 (borderline note, "
      "run328C max 405ms \u306f\u95c7\u5024\u5185\u306e\u4e0a\u632f\u308c\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002")

ilog = ("- 2026-09-07: **falsify \u7b2c152\u56de**\u300208:03 JST tick\u3002HEAD d8f6902 = bench \u7b2c138\u56de (07:53, 7\u6642\u53f0 run327) "
        "= remote net-kotobase/main \u4e00\u81f4 (fetch + rev-parse \u6bd4\u8f03; worktree detached HEAD \u306e\u305f\u3081 git pull --ff-only \u4e0d\u53ef, "
        "fetch \u7cfb\u3067\u53d6\u308a\u8fbc\u307f)\u3002live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002host load1 31.91 (08:01 uptime) "
        "\u2192 83.69 (08:03 \u6e2c\u5b9a\u6642, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057 production HTTP "
        "\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (gate \u5916)\u3002\u203bpre-run monitor NEXT\u300cK-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u300d\u306f stale "
        "(rank \u7b2c90\u56de\u5e2f artifact) \u2014 true progressive NEXT \u306f\u73fe\u5728\u6642\u523b\u5e2f\u306e current-band n-add \u3067\u3001\u524d tick "
        "(bench \u7b2c138\u56de) \u304c run327 \u3067 7\u6642\u53f0\u3092\u6d88\u5316\u6e08\u307f\u3001\u672c tick \u306f\u73fe\u6642\u523b\u5e2f 8\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u3068\u3057\u3066 "
        "\u6b21 run ID run328 \u3092\u5b9f\u65bd\u3002K-Z3 8\u6642\u53f0 run328A\u2013C \u3092\u672c tick \u5b9f\u6e2c (\u540c\u6e2c\u5b9a\u6cd5 n=20\u00d73 + landing control, "
        "\u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50, 08:03:41 JST, \u5168 80/80 200): A cold 1/20 (1.084s idx7 \u5358\u767a\u6563\u767a) "
        "p50 176.0ms / B 0/20 p50 139.1ms / C 0/20 p50 186.0ms / control (kotobase.net/signup) 0/20 p50 146.5ms max 235.9ms "
        "\u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4 search \u5074\u306b\u5c40\u5728 \u2014 search cold 1/60 (~1.7%) \u4f4e\u4f4d\u5e2f\u3001"
        "\u6563\u767a\u5358\u767a\u578b\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u7d99\u7d9a (heavy run271A 6/20 \u578b\u306f run271A \u4ee5\u964d 53 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe)\u3002"
        "8\u6642\u53f0 (9/7) \u5e2f\u521d\u8a08\u6e2c\u3001host load \u9ad8\u9a30 (83) \u3067 p50 \u4e0a\u632f\u308c (139\u2013186ms) \u306e borderline note \u4ed8\u304d\u3060\u304c "
        "max 405ms \u672a\u6e80\u3067 cold \u95c7\u5024\u5224\u5b9a 1/60 \u306f\u78ba\u5b9a\u7684\u3002\u8a73\u7d30\u306f K-Z3 evidence \u6b04 (L279 \u672b\u5c3e\u8ffd\u8a18)\u3002"
        "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002")

with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# sanity: confirm L279 is the K-Z3 row
assert "| K-Z3 |" in lines[278], "L279 not K-Z3 row"
# append evidence at END of K-Z3 cell line
lines[278] = lines[278].rstrip("\n") + ev + "\n"

# find the '## Iteration log' line; insert ilog right after it (newest-first)
ilog_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        ilog_idx = i
        break
assert ilog_idx is not None, "Iteration log header not found"
lines.insert(ilog_idx + 1, ilog + "\n")

with io.open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("OK inserted")
print("new_total_lines=", len(lines))