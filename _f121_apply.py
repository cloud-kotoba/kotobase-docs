FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(FN, encoding="utf-8").read().split("\n")

anchor = "第107回, K-Z3 23時台 n 積み増し run264A–C"
idx = None
for i, ln in enumerate(lines):
    if anchor in ln:
        idx = i
        break
if idx is None:
    raise SystemExit("anchor not found")

entry = (
 " falsify 2026-09-06 (第121回, K-Z3 23時台 n 積み増し run266A–C — run264/265 は bench 第107回/cosientist 第116回が先行使用のため run266 に読替 (run216/run256/run263 前例で 23時台内の独立 2 計測, 本測 23:47)。"
 "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 23:47:12–23:47:27 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 13.69 (23:47 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ):"
 " cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run266A 単発 1.2092s (19番目 散発) p50 0.083s warm_p50 0.083s / run266B cold 0/20 p50 0.064s max 0.127s / run266C cold 0/20 p50 0.069s max 0.109s,"
 " control (kotobase.net/signup) cold 0/20 p50 0.062s max 0.118s 完全静穏で control 分離成立、cold 群は search 側に局在。"
 "run266A 単発は B/C 0/20 + control 0/20 で即消失し run259A/261A/262A/B/264A 型「帯内 1 窓即消失」散発単発型継続 (run260A 8/20, run263A 5/20 heavy クラスタの再現なし — 散発減弱方向続行)。"
 "23時台通算 = falsify run260 (8/60) + bench run259 (4/60) + falsify run261 (3/60) + bench run262 (2/60) + falsify run263 (5/60) + bench run264 (1/60) + cosientist run265 (1/60) + 本 tick run266 (1/60) = 25/480 (~5.2%) で 8 セット連続 cold>0 — "
 "深夜帯 23時台 (traffic 最低帯) で cold 連続出現 (散発減弱継続) は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
 "ただし 8 セットとも「帯内 1 窓即消失」型で帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
)

lines.insert(idx + 1, entry)
open(FN, "w", encoding="utf-8").write("\n".join(lines))
print("inserted after line", idx + 2)