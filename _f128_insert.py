import io
FN="query-cosientist.md"
INS=" falsify 2026-09-07 (第128回, K-Z3 1時台深夜帯 n-add run282A-C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 01:47:48-01:48:33 JST, 全 80/80 200, host load1 37-44 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外): run282A cold(>=0.5s) 0/20 p50 45ms max 180ms / run282B cold 0/20 p50 64ms max 134ms / run282C cold 1/20 (単発散発 1.396s) p50 76ms max 1396ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 66ms max 241ms と静穏で control 分離成立、cold 群は search 側に局在。run282C 単発 1.396s は A/B 0/20 + control 0/20 で即消失「帯内 1 窓即消失」パターンと整合。1時台通算 run275..282 で 13/480 (~2.7%) の 8 セット連続 cold>0、散発単発型継続、heavy (run271A 6/20) 非再現、traffic 依存説への反証継続。status 判定は rank に委ねる (rank 専門)。"

lines=open(FN, encoding="utf-8").read().split("\n")
# locate K-Z3 row (0-based) by prefix
idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=i
        break
assert idx is not None, "K-Z3 row not found"
# append at END of that row line
lines[idx]=lines[idx]+INS
open(FN,"w",encoding="utf-8").write("\n".join(lines))
print("inserted at line", idx+1)