#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")
idx=278  # line 279
line=lines[idx]

ev=" bench 2026-09-07 (第142回, K-Z3 10時台 n-add run334A\u2013C, 同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 10:25:48\u201310:25:56 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 88.9 (production HTTP 実測のため gate 外), secret 不含 \u2014 curl のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) \u2014 run334A cold 2/20 (0.9399s/0.9615s \u653c\u6563\u30da\u30a2) p50 57.4ms / B cold 0/20 p50 54.7ms / C cold 0/20 p50 46.4ms, control (kotobase.net/signup) cold 0/20 p50 42.7ms max 314.3ms \u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4 search \u5074\u306b\u5c40\u5728\u3002run334A \u6563\u6563\u30da\u30a2\u306f B/C 0/20 + control 0/20 \u3067\u5373\u6d88\u5931\u3057 run333-indep A \u5358\u767a\u76f4\u5f8c\u306e\u6563\u767a\u5358\u767a/\u30da\u30a2\u578b\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u7d99\u7d9a (heavy run271A 6/20 \u578b\u306f 10\u6642\u53f0\u5e2f\u5185\u3067\u306f\u91cd\u307f\u518d\u73fe\u306a\u3057). 10\u6642\u53f0 (9/7) \u901a\u7b97 = falsify154-run332 (4/60) + bench141-run333 (5/60) + falsify155-run333-indep (1/60) + \u672c tick run334 (2/60) = 12/240 (~5.0%) \u4e2d\u4f4d\u5e2f\u5bc4\u308a\u3001run331A heavy 9/20 \u521d\u518d\u51fa\u73fe\u306e\u5f31\u301c\u4e2d\u4f4d\u5f8c\u7d9a (heavy >=6/20 \u306b\u306f\u81f3\u3089\u305a\u3001\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u3078\u53ce\u675f\u65b9\u5411). host load 88.9 \u306e p50 \u306f warm \u7fa4 46\u201357ms \u3068\u6982\u306d\u9759\u7a4f\u5bc4\u308a (control p50 42.7ms \u3068\u540c\u6c34\u6e96) \u3067\u5206\u6790\u6cd5\u306b\u5f71\u97ff\u306a\u3057\u3001cold \u5224\u5b9a 2/60 \u306f control \u5b8c\u5168\u9759\u7a4f\u3067\u78ba\u5b9a\u7684\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"

anchor="\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
# append to END of line 279
assert line.endswith(anchor), "anchor not at end: "+line[-80:]
lines[idx]=line+ev
open(path,"w").write("\n".join(lines))
print("appended. new len line279:", len(lines[idx]))