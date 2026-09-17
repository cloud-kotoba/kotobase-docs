import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = io.open(p, encoding="utf-8").read()
anchor = "  計測を bench 担当として即実行)。\n"
assert s.count(anchor) == 1, s.count(anchor)
block = ("cosientist 2026-09-05 (第49回, K-Z3 14時台 n 積み増し run152A–C — NEXT 委ねるに従い継続, 同測定法, "
 "production HTTP 実測のため gate 外, secret 不含): 14:24–14:25 JST, n=20 × 3 + landing control, 別接続 curl, Tokyo, "
 "全 80/80 200: run152A cold(>=0.5s) 4/20 (0.915/1.028/1.099/1.149s 散発配置, warm p50 0.155s) / run152B cold 1/20 "
 "(1.388s, warm p50 0.150s) / run152C cold 0/20 (p50 0.169s) — 14時台通算 cold 5/60 ~8.3%。landing control "
 "(kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.096s と静穏で control 分離成立、cold 群は search 側に局在。"
 "13時台 (falsify run151 4/60 ~6.7% + bench run47 7/60 低位散発/多発混在) と同程度の低位散発型 — 帯別分布 11時台 ~16.7% / "
 "12時台 ~8.3% / 13時台 ~6.7% / 14時台 ~8.3% で日中帯全般に 1 桁後半〜低位 10% 台の散発が底として分布、多発型 (run47A 型) は"
 "帯内突発。status 判定は rank に委ねる。NEXT: 委ねる。NEXT: K-Z3 14時台 n 積み増し継続 (限界利得低下のため rank 判断優先)。\n")
s = s.replace(anchor, anchor + block, 1)
io.open(p, "w", encoding="utf-8").write(s)
print("inserted ok, new size", len(s))
