p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p).read().split("\n")
INS=" falsify 2026-09-07 (第133回, K-Z3 3時台(深夜帯) 帯初計測 run291A–C — rank 第127回 NEXT「K-Z3 current-band n-add (run291)」に従い 3時台 n 積み増し (次 run ID run291), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 03:01:4x–03:01:5x JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 20.99 (03:01 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run291A cold 単発散発 0.9367s (9番目 散発) p50 0.0482s max 0.9367s warm 群 0.0398–0.1523s / run291B cold 単発散発 1.6194s (13番目 散発) p50 0.0452s max 1.6194s / run291C cold 0/20 p50 0.0496s max 0.1523s, control (kotobase.net/signup) cold 0/20 p50 0.0423s max 0.0551s 完全静穏で control 分離成立、cold 群は search 側に局在。run291A/B 各単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (bench run290A 単発 1.442s (02:53) の ~8 分後 3時台の両 run 各単発再出現、heavy クラスタは run271A 以降 18 セット非再現)。3時台 帯初計測 cold 2/60 (~3.3%) — deep-night 累計 run275..291 = 24/1080 (~2.2%) の 18 セットで低位帯水準継続 — 深夜最低帯 (traffic 最低) での cold 散発再出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし control 分離成立・cold 2/60 薄散発 (両 run 各単発) で機構判定には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
anchor=" falsify 2026-09-07 (第132回"
idx=None
for i,l in enumerate(lines):
    if l.startswith(anchor) and "run290" in l:
        idx=i
if idx is None:
    raise SystemExit("ANCHOR_NOT_FOUND")
lines[idx]+=INS
open(p,"w").write("\n".join(lines))
print("inserted after line",idx)