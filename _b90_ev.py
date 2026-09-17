#!/usr/bin/env python3
MD="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(MD,encoding="utf-8").read().split("\n")
# find K-Z3 row
idx=None
for n,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=n; break
print("KZ3_LINE=", idx+1)
row=lines[idx]
# The falsify 第90回 entry ends the row: tail contains "...status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
tail_anchor="status \u79fb\u884c\u306a\u3057 (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a (curl \u306e\u307f)\u3002"
# there may be multiple such; need the LAST falsify90 one. Use rfind within row.
pos=row.rfind("15\u6642\u53f0\u901a\u7b97 (run215+run216) 3/120")
print("f90_anchor_pos=",pos)
if pos<0:
    pos=row.rfind(tail_anchor)
    print("fallback tail pos=",pos)
# append bench 89 run217 evidence after the falsify90 tail (end of row)
ev=(
 " bench 2026-09-06 (\u7b2c89\u56de, K-Z3 15\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 \u2014 falsify \u7b2c90\u56de (run216, 15:16) \u3068 "
 "run ID \u885d\u7a81\u3057\u672c\u5206\u3092 run217A\u2013C \u3068\u3057\u3066\u72ec\u7acb\u8a08\u6e2c\u3068\u3057\u3066\u8a18\u9332, "
 "\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, "
 "15:09:47\u201315:09:56 JST, \u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test, "
 "host load1 77.81 (gate 7.5 \u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): "
 "run217A cold(>=0.5s) 1/20 (0.911s 3\u756a\u76ee\u306e\u5358\u767a) p50 43.1ms / run217B cold 0/20 "
 "p50 47.0ms / run217C cold 0/20 p50 53.5ms \u2014 landing control (kotobase.net/signup, \u540c\u6642\u523b, "
 "n=20, \u5168 200) \u306f cold 0/20 p50 51.0ms max 249.0ms \u3068\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001"
 "cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002run217 \u5358\u767a\u306f run216 (falsify \u7b2c90\u56de) \u3068\u540c\u578b\u306e"
 "\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u30d1\u30bf\u30fc\u30f3\u3002"
 "15\u6642\u53f0\u901a\u7b97 run215 (2/60) + run216 (1/60) + run217 (1/60) = 4/180 (~2.2%) \u4f4e\u4f4d\u5e2f\u6b8b\u754c\u7d9a\u304f\u3002"
 "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
)
lines[idx]=row+ev
open(MD,"w",encoding="utf-8").write("\n".join(lines))
print("EVIDENCE_APPENDED total_run217_count_after:", open(MD,encoding='utf-8').read().count("run217"))