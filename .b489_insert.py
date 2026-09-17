# -*- coding: utf-8 -*-
import io

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(P, encoding="utf-8") as f:
    txt = f.read()

EVID = (" bench 2026-09-08 (\u7b2c213\u56de, K-Z3 18\u6642\u53f0(9/8) n \u7a4d\u307f\u5897\u3057 run489A\u2013C \u2014 falsify \u7b2c218\u56de (17:58, 17\u6642\u53f0 run488 cold 6/60) \u5f8c\u306e\u7d9a\u884c\u67a0, "
        "\u73fe\u5728\u6642\u523b\u5e2f 18\u6642\u53f0 (9/8) \u5e2f\u5185 1 \u30bb\u30c3\u30c8\u76ee (run488 \u306f 18:00\u201318:02 \u8a08\u6e2c\u306a\u304c\u3089 17\u6642\u53f0\u3078 fold \u6e08\u307f\u306e\u305f\u3081 18\u6642\u53f0\u306f\u672a\u8a08\u6e2c), "
        "\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50, \u6b63 endpoint search.kotobase.net/search?q=test, "
        "18:10:45\u201318:11:38 JST, \u5168 80/80 200, host load1 29.89 (18:08 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b \u2014 curl + python stats \u306e\u307f): "
        "cold(>=0.5s) 3/0/4 per 20 = 7/60 (~11.7%) \u2014 run489A cold 3/20 (0.6710/0.8558/1.3021s \u6563\u767a\u914d\u7f6e) p50 170.3ms / run489B cold 0/20 p50 142.8ms max 333.1ms / run489C cold 4/20 (0.6862/0.7693/0.9681/1.0870s \u5206\u6563\u914d\u7f6e) p50 296.6ms \u2014 "
        "landing control (kotobase.net/signup, \u540c\u6642\u523b, n=20, \u5168 200) \u306f cold 1/20 (0.5965s \u95d8\u5024\u304e\u308a\u304e\u5883\u754c\u5024) p50 139.4ms max 596.5ms \u3067 control \u306b cold 1 \u4ef6\u51fa\u73fe\u3057 control \u5206\u96e2\u306f borderline not-separated \u503e\u5411 "
        "(search \u5074 cold 7/60 \u81ea\u4f53\u306f 0.671\u20131.302s \u3067\u95d8\u5024\u6c7a\u5b9a\u7684\u3060\u304c control \u306b\u3082 0.597s \u304c 1 \u4ef6\u51fa\u305f\u305f\u3081\u6a5f\u69cb\u5224\u5b9a\u3068\u3057\u3066\u306f\u5f31\u3044 + A/C p50 (170/297ms) \u306f host load ~30 high tick \u306e\u4e0a\u632f\u308c\u6df7\u5165\u53ef\u80fd\u3067 borderline \u6ce8\u8a18\u4ed8\u304d). "
        "run489A/C \u306b cold \u304c\u540c\u6642\u591a\u767a (A 3/20 + C 4/20 = 7/60) \u3057 B 0/20 \u3067 17\u6642\u53f0 (28/240 ~11.7%) \u306b\u7d9a\u304f\u65e5\u4e2d\u5e2f\u9ad8\u4f4d (18\u6642\u53f0 (9/8) \u5e2f\u5185 1 \u30bb\u30c3\u30c8\u76ee cold 7/60 ~11.7%), "
        "traffic \u4f9d\u5b58\u8aac\u306e\u65e5\u4e2d\u5e2f\u65b9\u5411\u652f\u6301\u7d99\u7d9a, \u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u306e\u5bfe\u6bd4\u4e0d\u5909. status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580).")

# --- evidence append to the K-Z3 row (line starting with "| K-Z3 |") ---
anchor = "| K-Z3 |"
idx = txt.find(anchor)
assert idx != -1, "K-Z3 row not found"
row_end = txt.find("\n", idx)
assert row_end != -1
row = txt[idx:row_end]
txt = txt[:row_end] + EVID + txt[row_end:]

# --- iter-log insert right after "## Iteration log" header ---
hdr = "## Iteration log\n"
hidx = txt.find(hdr)
assert hidx != -1, "Iteration log header not found"
insert_at = hidx + len(hdr)
ILOG = ("- 2026-09-08: bench \u7b2c213\u56de\u300218:11 JST tick\u3002HEAD bf18472 = falsify \u7b2c218\u56de (17:58, K-Z3 17\u6642\u53f0 run488 cold 6/60; NEXT \u59d4\u306d\u308b \u2192 \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af run489) = remote net-kotobase/main \u4e00\u81f4 "
        "(fetch + rev-parse \u9755\u96e2 0; detached HEAD \u306e\u305f\u3081 fetch \u7cfb\u3067\u53d6\u8fbc; terminal stdout \u7a7a=\u65e2\u77e5\u306e\u305f\u3081\u72b6\u614b\u78ba\u8a8d\u30fb\u8a08\u6e2c\u51fa\u529b\u306f\u30d5\u30a1\u30a4\u30eb\u7d4c\u7531; "
        "pre-run monitor NEXT\u300c\u59d4\u306d\u308b\u3002NEXT: K-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u884c\u3002\u300d\u306f stale (rank \u5e2f artifact \u524d\u4f8b) \u2014 true progressive NEXT \u306f iter-log HEAD \u9023\u9396 (falsify \u7b2c218\u56de NEXT \u59d4\u306d\u308b \u2192 \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057, \u6b21 run ID \u306f run489)). "
        "host load1 29.89 (18:08 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916\u3002live smoke 200 (/, /signup; pre-run \u8a08\u6e2c 200)\u3002"
        "K-Z3 18\u6642\u53f0 run489A-C \u3092\u5b9f\u6e2c (\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50, \u6b63 endpoint search.kotobase.net/search?q=test, 18:10:45\u201318:11:38 JST, "
        "\u5168 80/80 200, secret \u4e0d\u542b \u2014 curl + python stats \u306e\u307f): cold(>=0.5s) 3/0/4 per 20 = 7/60 (~11.7%) \u2014 run489A \u6563\u767a 3/20 / run489B 0/20 / run489C \u6563\u767a 4/20, "
        "landing control (kotobase.net/signup) cold 1/20 (0.5965s \u5883\u754c\u5024) \u3067 control \u5206\u96e2 borderline not-separated \u503e\u5411 (search cold 7/60 \u306f\u95d8\u5024\u6c7a\u5b9a\u7684)\u3002"
        "18\u6642\u53f0 (9/8) \u5e2f\u5185 1 \u30bb\u30c3\u30c8\u76ee cold 7/60 ~11.7% \u306f 17\u6642\u53f0 (28/240 ~11.7%) \u3068\u540c\u6c34\u6e96\u306e\u65e5\u4e2d\u5e2f\u9ad8\u4f4d\u7d99\u7d9a, traffic \u4f9d\u5b58\u8aac\u306e\u65e5\u4e2d\u5e2f\u65b9\u5411\u652f\u6301\u7d99\u7d9a, \u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u306e\u5bfe\u6bd4\u4e0d\u5909\u3002"
        "status \u5224\u5b9a\u306f rank \u5c02\u9580\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002\u8a73\u7d30\u306f K-Z3 evidence \u6b04 (L279 \u672b\u5c3e\u8ffd\u8a18)\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057\u7d9a\u884c, \u6b21 run ID \u306f run490)\u3002\n")
txt = txt[:insert_at] + ILOG + txt[insert_at:]

with io.open(P, "w", encoding="utf-8", newline="") as f:
    f.write(txt)
print("INSERT_OK ev_anchor_idx=%d ilog_insert_at=%d" % (idx, insert_at))