# -*- coding: utf-8 -*-
import sys
SRC="/tmp/qc_head.md"
DST="/tmp/qc_new.md"
KZ3_ANCHOR="| K-Z3 | worker |"
ILOG_ANCHOR="## Iteration log"
EVIDENCE=(
" bench 2026-09-08 (bench \u7b2c224\u56de, K-Z3 22\u6642\u53f0 n \u7a4d\u304d\u589e\u3057 run509A-C"
" \u2014 rank \u7b2c220\u56de NEXT\u300cK-Z3 \u73fe\u5728\u6642\u523b\u5e26 22\u6642\u53f0 n \u7a4d\u304d\u589e\u3057\u7d9a\u884c,"
" " \u6b21 run ID \u306f run509 \u4f7f\u7528\u300d\u306e run509 \u67a0,"
" " \u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control,"
" " \u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50,"
" " \u6b63 endpoint search.kotobase.net/search?q=test, 22:31\u201322:33 JST,"
" " \u5168 80/80 200, host load1 12.89 (22:30 uptime \u5b9f\u6e2c, gate 7.5 \u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916,"
" " secret \u4e0d\u542b \u2014 curl + python stats \u306e\u307f):"
" " cold(>=0.5s) 5/0/1 per 20 =6/60 (~10.0%)"
" " \u2014 run509A \u6563\u6563\u5e03\u30af\u30e9\u30b9\u30bf 5/20 (pos1 1.3071s / pos5 1.3559s / pos10 1.3384s / pos12 1.5887s / pos17 2.1175s) p50 142.2ms"
" " / run509B 0/20 p50 66.1ms / run509C \u5358\u767a 1/20 (pos3 1.6515s) p50 73.8ms,"
" " control (kotobase.net/signup) cold 0/20 p50 118.8ms max 362.8ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb, cold \u7fa4 search \u5074\u5c40\u5728\u3002"
" "run509A \u6563\u6563\u5e03\u30af\u30e9\u30b9\u30bf 5/20 \u306f B 0/20 \u3067\u5373\u6d88\u5931\u3057\u300c\u5e26\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u578b\u7d9a\u7d9a (run508A 6/20 (22:01) \u306e ~30 \u5206\u5f8c\u518d\u4e0a\u632f\u308c, heavy>=6/20 \u306f\u672c tick \u975e\u518d\u73fe)\u3002"
" "22\u6642\u53f0 (9/8) \u901a\u7b97 = run508 (7/60) + \u672c tick run509 (6/60) =13/120 (~10.8%) 2 \u30bb\u30c3\u30c8"
" " \u2014 21\u6642\u53f0 (26/240 ~10.8%)\u3068\u540c\u6c34\u6e96\u306e\u9ad8\u4f4d\u5e26\u7d9a\u7d9a, traffic \u4f9d\u5b58\u8aac\u306e\u665a\u5074\u30c8\u30e9\u30f3\u30b8\u30b7\u30e7\u30f3\u5e26\u65b9\u5411\u652f\u6301\u7d9a\u7d9a, \u6df1\u591c\u5e26 ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u306e\u5bfe\u6bd4\u4e0d\u5909\u3002"
" "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
)
ILOG_ENTRY=(
"- 2026-09-08: bench \u7b2c224\u56de\u3002"
"22:33 JST tick\u3002HEAD 27b0da5 = rank \u7b2c220\u56de (22:05,"
" K-Z3 21hr fold + 22hr n-run509 NEXT)= remote net-kotobase/main \u4e00\u81f4"
" " (git fetch + rev-parse \u6bd4\u8f03 \u5f6e\u79b1 0; detached HEAD \u306e\u305f\u3081 fetch \u7cfb\u3067\u53d6\u8fbc;"
" " terminal foreground stdout \u7a7a=\u65e2\u77e5\u306e\u305f\u3081 \u72b6\u614b\u78ba\u8a8d\u30fb\u8a08\u6e2c\u51fa\u529b\u306f\u30d5\u30a1\u30a4\u66f8\u51fa\u7d4f\u7531;"
" " worktree doc clean + run509 \u672a\u4f7f\u7528\u78ba\u8a8d\u6e08 (HEAD 27b0da5 \u306e run509 \u51fa\u73fe\u306f rank \u7b2c220\u56de NEXT\u300c\u6b21 run ID \u306f run509 \u4f7f\u7528\u300d\u306e\u672a\u6765\u53c2\u7167\u306e\u307f\u3067\u5b9f\u6e2c commit \u306a\u3057"
" " \u2014 run509 \u67a0\u3092\u672c tick \u5b9f\u65bd)))\u3002"
" "pre-run monitor NEXT\u300c\u59d4\u306d\u308b\u3002NEXT: K-Z3 \u6df1\u591c\u5e26 23\u6642\u53f0 n \u7a4d\u304d\u589e\u3057\u7d9a\u7d9a\u3002\u300d\u306f stale (rank \u5e26 artifact) \u2014"
" " true progressive NEXT \u306f iter-log HEAD \u9023\u9396 (rank \u7b2c220\u56de NEXT\u300cK-Z3 \u73fe\u5728\u6642\u523b\u5e26 22\u6642\u53f0 n \u7a4d\u304d\u589e\u3057\u7d9a\u884c, \u6b21 run ID \u306f run509 \u4f7f\u7528\u300d)\u3002"
" "host load1 12.89 (22:30 uptime \u5b9f\u6e2c, gate 7.5 \u8d85\u904e)\u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916\u3067\u5b9f\u65bd\u3002"
" "live smoke 200 (/, /signup); pre-run \u8a08\u6e2c + \u672c tick \u5b9f\u6e2c 200)\u3002"
" "K-Z3 22\u6642\u53f0 n \u7a4d\u304d\u589e\u3057 run509A-C \u3092\u5b9f\u6e2c (\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control,,"
" " \u5225\u63a5\u7d9a curl,,cold>=0.5s,,nearest-rank p50,,\u6b63 endpoint search.kotobase.net/search?q=test,,"
" "22:31:10\u201322:33:05 JST,,\u5168 80/80 200,,secret \u4e0d\u542b \u2014 curl + python stats \u306e\u307f): "
" "cold(>=0.5s) 5/0/1 per 20 =6/60 (~10.0%) \u2014 run509A \u6563\u6563\u5e03\u30af\u30e9\u30b9\u30bf 5/20 (pos1 1.3071s / pos5 1.3559s / pos10 1.3384s / pos12 1.5887s / pos17 2.1175s) p50 142.2ms / run509B 0/20 p50 66.1ms / run509C \u5358\u767a 1/20 (pos3 1.6515s) p50 73.8ms,"
" " control (kotobase.net/signup) cold 0/20 p50 118.8ms max 362.8ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb,, cold \u7fa4 search \u5074\u5c40\u5728\u3002"
" "run509A \u6563\u6563\u5e03\u30af\u30e9\u30b9\u30bf 5/20 \u306f B 0/20 \u3067\u5373\u6d88\u5931\u3057\u300c\u5e26\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u578b\u7d9a\u7d9a (run508A 6/20 (22:01) \u306e ~30 \u5206\u5f8c\u518d\u4e0a\u632f\u308c,, heavy>=6/20 \u306f\u672c tick \u975e\u518d\u73fe)\u3002"
" "22\u6642\u53f0 (9/8) \u901a\u7b97 = run508 (7/60) + \u672c tick run509 (6/60) =13/120 (~10.8%) 2 \u30bb\u30c3\u30c8 \u2014 21\u6642\u53f0 (26/240 ~10.8%)\u3068\u540c\u6c34\u6e96\u306e\u9ad8\u4f4d\u5e26\u7d9a\u7d9a,"
" " traffic \u4f9d\u5b58\u8aac\u306e\u665a\u5074\u30c8\u30e9\u30f3\u30b8\u30b7\u30e7\u30f3\u5e26\u65b9\u5411\u652f\u6301\u7d9a\u7d9a,, \u6df1\u591c\u5e26 ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u306e\u5bfe\u6bd4\u4e0d\u5909\u3002"
" "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002\u8a73\u7d30\u306f K-Z3 evidence \u6b04 (L279 \u672b\u5c3e\u8ffd\u8a18)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002"
" "NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148;\u30d5\u30a1\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e26 22\u6642\u53f0 n \u7a4d\u304d\u589e\u3057\u7d9a\u884c, \u6b21 run ID \u306f run510 \u4f7f\u7528)\u3002"
)

def stripcomb(txt):
    return txt.replace("\u0308","")

def main():
    t=open(SRC,encoding="utf-8").read()
    i=t.index(KZ3_ANCHOR)
    j=t.index("\n",i)
    t=t[:j]+stripcomb(EVIDENCE)+t[j:]
    k=t.index(ILOG_ANCHOR)
    l=t.index("\n",k)
    t=t[:l+1]+stripcomb(ILOG_ENTRY)+"\n"+t[l+1:]
    open(DST,"w",encoding="utf-8").write(t)
    print("OK kz3_at=%d ilog_at=%d" % (i+1,k+1))

if __name__ == "__main__":
    main()