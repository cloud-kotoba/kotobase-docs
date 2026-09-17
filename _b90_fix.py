#!/usr/bin/env python3
MD="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data=open(MD,encoding="utf-8").read()

old_entry_start="- 2026-09-06: bench \u7b2c89\u56de\u300215:09 JST tick\u3002"
i=data.find(old_entry_start)
print("FOUND_OLD=", i>=0)
if i>=0:
    j=data.find("\n", i)
    old_block=data[i:j]
    new_block=(
        "- 2026-09-06: bench \u7b2c89\u56de\u300215:09 JST tick\u3002"
        "worktree detached HEAD \u306e\u305f\u3081 "
        "fetch net-kotobase + rev-parse \u6bd4\u8f03\u3067\u53d6\u308a\u8fbc\u307f "
        "(\u672c tick \u4e2d\u306b falsify \u7b2c90\u56de aa1260a \u304c \u5165\u308a\u3001\u6700\u7d42\u72b6\u614b\u306f main \u5148\u7aef aa1260a = falsify \u7b2c90\u56de\u306b\u4e00\u81f4)\u3002"
        "live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002"
        "host load1 77.81 (gate 7.5 \u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057\u300c"
        "host busy (load1 77.81)\u300d\u3092\u8a18\u9332\u3002"
        "\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (production HTTP \u5b9f\u6e2c, gate \u5916): K-Z3 15\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 "
        "\u2014 \u672c tick \u6e2c\u5b9a (15:09 \u5b9f\u6e2c\u3001run216 \u3068\u3057\u3066\u53d6\u5f97) \u306f falsify \u7b2c90\u56de (15:16 \u5b9f\u6e2c) \u3068 "
        "run ID run216 \u304c\u885d\u7a81\u3002fleet \u524d\u4f8b (run105/run123/run124) \u306b\u5f93\u3044\u672c\u5206\u3092 run217A\u2013C \u306b"
        "\u8aad\u307f\u66ff\u3048\u3066\u8a18\u9332 (\u4e21\u8005\u306f\u540c\u4e00\u6642\u9593\u5e2f\u306e\u72ec\u7acb 2 \u8a08\u6e2c)"
        ": run217A cold(>=0.5s) 1/20 (0.911s 3\u756a\u76ee\u306e\u5358\u767a) p50 43.1ms / run217B cold 0/20 p50 47.0ms / "
        "run217C cold 0/20 p50 53.5ms \u2014 landing control (kotobase.net/signup, \u540c\u6642\u523b, n=20, \u5168 200) \u306f "
        "cold 0/20 p50 51.0ms max 249.0ms \u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002"
        "run217 \u5358\u767a\u306f run216 (falsify \u7b2c90\u56de) \u3068\u540c\u578b\u306e\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u30d1\u30bf\u30fc\u30f3\u3002"
        "15\u6642\u53f0\u901a\u7b97 run215 (2/60) + run216 (falsify 1/60) + run217 (\u672c\u5206 1/60) = 4/180 (~2.2%) \u4f4e\u4f4d\u5e2f\u6b8b\u754c\u7d9a\u304f\u3002"
        "status \u79fb\u884c\u306a\u3057 (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a (curl \u306e\u307f)\u3002"
        "NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a)\u3002"
    )
    data=data[:i]+new_block+data[j:]
    open(MD,"w",encoding="utf-8").write(data)
    print("LOG_FIXED len_old=",len(old_block),"len_new=",len(new_block))
else:
    print("OLD_ENTRY_NOT_FOUND")