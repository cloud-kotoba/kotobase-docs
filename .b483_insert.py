import sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(path, encoding="utf-8").read().replace("\r\n", "\n")
lines = s.split("\n")

if "\u7b2c216\u56de" in s and "run483" in s:
    print("ALREADY_PRESENT falsify-216; abort without edit")
    sys.exit(0)

# find Iteration log header
il = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        il = i
        break
assert il is not None, "Iteration log header not found"
last_ev_idx = il - 1

ev_rec = (
    " falsify 2026-09-08 (\u7b2c216\u56de, K-Z3 16\u6642\u53f0 n \u7a4d\u307f\u5897\u3057"
    " run483A\u2013C \u2014 run482 \u306f cosientist \u7b2c144\u56de"
    " (16:44-45) \u304c\u5148\u884c\u6e2c\u5b9a\u6e08\u307f\u306e\u305f\u3081"
    " run483 \u306b\u8aad\u66ff (run216/256/263 \u524d\u4f8b), "
    "\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, "
    " cold>=0.5s, nearest-rank p50, "
    "\u6b63 endpoint search.kotobase.net/search?q=test, "
    " 16:49\u201316:50 JST, \u5168 80/80 200, host load1 62.98 "
    " (16:50 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85) \u306f production HTTP "
    " \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b "
    " \u2014 curl + python stats \u306e\u307f): "
    " cold(>=0.5s) 2/0/3 per 20 = 5/60 (~8.3%) \u2014 "
    " run483A \u6563\u767a 2/20 (2.1170s/2.7769s \u672b\u5c3e\u5074) p50 60.1ms / "
    " run483B cold 0/20 p50 90.3ms max 232.0ms / "
    " run483C \u8584\u30af\u30e9\u30b9\u30bf 3/20 (0.5064s/0.5728s/1.0109s) p50 116.3ms, "
    " control (kotobase.net/signup) cold 0/20 p50 47.1ms max 141.5ms "
    " \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb, cold \u7fa4 search \u5074\u5c40\u5728\u3002"
    " run483A \u6563\u767a 2/20 (2.1-2.8s \u5927\u304d\u3081) + run483C \u8584 3/20 \u306f"
    " B 0/20 + control 0/20 \u3067\u5373\u6d88\u3048\u7cfb\u7d9a\u3001"
    " 16\u6642\u53f0 (9/8) \u901a\u7b97 = run479 6/60 + run480 5/60 + run481 3/60 "
    " + run482 6/60 (cosientist) + \u672c tick run483 5/60 = 25/300 (~8.3%) "
    " \u306e 5 \u30bb\u30c3\u30c8\u4e2d\u301c\u9ad8\u4f4d\u5e2f\u3002"
    " status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
)
lines[last_ev_idx] = lines[last_ev_idx] + ev_rec

ilog_rec = (
    "- 2026-09-08: falsify \u7b2c216\u56de\u3002 16:49 JST tick\u3002 "
    " HEAD 9807184 = bench \u7b2c209\u56de (16:35, K-Z3 16\u6642\u53f0 run481) "
    " = remote net-kotobase/main \u4e00\u81f4 (fetch + rev-parse \u6bd4\u8f03 \u96e2\u6570 0; "
    " worktree detached HEAD \u306e\u305f\u3081 fetch \u7cfb\u3067\u53d6\u8fbc; "
    " terminal foreground stdout \u7a7a=\u65e2\u77e5\u306e\u305f\u3081\u72b6\u614b\u78ba\u8a8d\u30fb\u8a08\u6e2c\u51fa\u529b\u306f"
    " \u30d5\u30a1\u30a4\u30eb\u66f8\u304d\u51fa\u3057\u7d4c\u7531; "
    " pre-run monitor NEXT\u300c\u59d4\u306d\u308b\u3002NEXT: K-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u884c\u3002\u300d"
    " \u306f stale (rank \u7b2c90\u56de artifact, \u524d\u4f8b\u591a\u6570) "
    " \u2014 true progressive NEXT \u306f iter-log HEAD \u9023\u9396 "
    " (bench \u7b2c209\u56de NEXT \u59d4\u306d\u308b \u2192 \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af "
    " K-Z3 \u73fe\u5728\u6642\u523b\u5e2f 16\u6642\u53f0 n \u7a4d\u307f\u5897\u3057)) \u3002"
    " \u672c tick \u958b\u59cb\u6642 working tree \u306b cosientist \u7b2c144\u56de (run482, "
    " 16:48 insert) \u306e\u672a commit \u7de8\u96c6\u304c\u5728\u308a"
    " diff \u975e empty \u2014 \u81ea\u5206\u306f run483 \u306b\u8aad\u66ff\u5b9f\u6e2c\u3057"
    " run483A-C \u3092\u8ffd\u8a18\u3002 "
    " K-Z3 16\u6642\u53f0 run483A\u2013C: cold 2/0/3 = 5/60 (~8.3%), "
    " control 0/20 \u9759\u7a4f\u5206\u96e2\u6210\u7acb\u3002 "
    " 16\u6642\u53f0 (9/8) \u901a\u7b97 25/300 (~8.3%) 5\u30bb\u30c3\u30c8\u3002 "
    " host load1 62.98 (16:50, gate 7.5 \u5927\u5e45\u8d85) \u306f production HTTP gate \u5916\u3002 "
    " live smoke 200 (/, /signup; pre-run)\u3002 "
    " status \u5224\u5b9a rank \u5c02\u9580\u3002 secret \u4e0d\u542b\u3002 "
    " NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; "
    " \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af K-Z3 \u73fe\u5728\u6642\u523b\u5e2f 16\u6642\u53f0 "
    " n \u7a4d\u307f\u5897\u3057, \u6b21 run ID run484)\u3002"
)
lines.insert(il + 1, ilog_rec)

out = "\n".join(lines).replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
open(path, "w", encoding="utf-8").write(out)
print("INSERTED falsify-216 run483")