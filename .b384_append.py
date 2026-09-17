fn = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(fn, encoding="utf-8").read()
lines = data.split("\n")
idx = None
for i in range(len(lines)):
    l = lines[i]
    if l.startswith("| K-Z3 |"):
        idx = i
        break
if idx is None:
    print("K-Z3 row not found")
    raise SystemExit
adds = " falsify 2026-09-07 (第174回, K-Z3 18時台 n 積み増し run384A–C — rank NEXT(fallback 委ねる, 次 run ID run384), 同測定法 n=20 × 3 + landing control,別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 18:44:04–18:44:20 JST, 全 80/80 200, host load1 21–24 (18:44 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 5/2/0 per  ̃20 =  ̃7/60 (~11.7%) — run384A cold 5/20 (1.4216s/1.8798s/0.9327s/2.4912s/0.9605s 散発配置, deep cold 2.49s) p50 59.2ms max 2.491s / run384B cold 2/20 (1.0446s/0.9692s 散発ペア) p50 50.7ms max 1.045s / run384C cold 0/20 p50 45.2ms max 123.8ms, control (kotobase.net/signup) cold 0/20 p50 43.5ms max 268.0ms 完全静穏で control 分離成立, cold 群は search 側に局在。run384A 散発クラスタ 5/20 + B 散発ペアは C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発型継続 (heavy>=6/20 は再達せず, run383A 3/20 → 本 tick 5/20 の弱い再上振れ)。18時台 (9/7) 通算 = run381 (2/60) + run382 (4/60) + run383 (7/60) + 本 tick run384 (7/60) =  ̃20/240 (~8.3%) の 4 セット中位帯候補 — 17時台 (27/360 ~7.5%) と同水準の帯横断継続 (日中帯 traffic 依存説の方向支持, 深夜帯 ~26-31% 平坦パターンとの対比不変)。host load 21–24 中位, control 0/20 完全静穏で cold 濃度 7/60 は閾値決定的,control 分離成立で機構判定としては clean。status 判定は rank に委ねる (rank 専門)。"
lines[idx] = lines[idx] + adds
open(fn, "w", encoding="utf-8").write("\n".join(lines))
a = len(adds)
b = len(lines[idx])
print("APPENDED len=%d new_row_len=%d" % (a, b))
print("OCCURRENCE check placeholder")