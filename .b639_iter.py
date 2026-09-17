import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    lines = f.readlines()

hdr = None
for i, l in enumerate(lines):
    if l.startswith("## Iteration log"):
        hdr = i
        break
assert hdr is not None, "header not found"
# header row and the separator row (|---|) come right after; newest entry is hdr+2
ins = hdr + 2
assert lines[ins].startswith("- 2026-"), "unexpected line at insertion point: " + lines[ins][:40]

entry = ("- 2026-09-16: falsify \u7b2c157\u56de (11:24 JST tick)\u3002HEAD 0fc2f379 = fetch \u5f8c "
         "net-kotobase/main \u5148\u7aef\u4e00\u81f4 (worktree detached HEAD \u306e\u305f\u3081 fetch + rev-parse "
         "\u6bd4\u8f03, \u4e57\u96e2 0)\u3002monitor: host load1 48.56 (11:24 pre-tick \u5b9f\u6e2c, gate 7.5 "
         "\u8d85\u904e \u2014 production HTTP \u5b9f\u6e2c\u306a\u3089 gate \u5916), live smoke 301/301 "
         "(kotobase.net/ \u2192 kotoba.cloud/docs/graph/, /signup)\u3002rank NEXT\u300cK-Z3 \u6df1\u591c\u5e2f "
         "23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u300d\u306f\u672c tick \u6642\u523b (11\u6642\u53f0) "
         "\u306e\u305f\u3081\u5f85\u6a5f\u4e0d\u53ef\u80fd \u2014 \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af "
         "(production HTTP \u5b9f\u6e2c) \u3067 K-Z3 11\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run639A-C \u3092\u5b9f\u65bd "
         "(\u540c\u6e2c\u5b9a\u6cd5 n=20 x3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, "
         "11:26:38-11:27:54 JST, \u5168 80/80 200): cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) - "
         "A \u8584\u30af\u30e9\u30b9\u30bf 4/20 (0.75-0.91s, \u5192\u982d 1-5 \u756a\u76ee + \u4e2d\u76e4 #14 "
         "\u518d\u71c3) p50 68.4ms / B \u5358\u767a 1/20 (1473.4ms) / C 0/20, control (kotoba.cloud/) "
         "0/20 p50 99.4ms max 227.7ms \u5b8c\u5168\u9759\u7a33\u3067 control \u5206\u96e2\u6210\u7acb\u3002"
         "11\u6642\u53f0 9/16 \u901a\u7b97 17/120 (~14.2%) \u4e2d\u4f4d\u5e26 (run638 ~20.0% + \u672c\u6e2c "
         "~8.3%; \u65e5\u6b21\u7cfb\u5217 6 \u65e5\u76ee spread ~11 \u500d\u7d99\u7d9a, K-Z4 \u6750\u6599)\u3002"
         "evidence \u306f K-Z3 \u4eee\u8aac\u884c\u672b\u5c3e\u306b\u8ffd\u8a18\u6e08\u307f (occurrence=1 "
         "\u78ba\u8a8d)\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
         "NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f "
         "K-Z3 \u73fe\u5728\u6642\u523b\u5e2f 11\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a, \u6b21 run ID "
         "\u306f run640 \u4f7f\u7528)\u3002secret \u4e0d\u542b (curl + python3 stats \u306e\u307f)\u3002\n")

lines.insert(ins, entry)

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("inserted at", ins + 1)
