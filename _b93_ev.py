import io

path = "query-cosientist.md"
s = open(path, encoding="utf-8").read()

ev = """本 tick は host load 32 の p50 上振れ (search p50 41–87ms, control p50 98ms) がみられるが cold 濃度判定 2/60 は閾値決定的。status 判定は rank に委ねる (rank 専門)。
bench 2026-09-06 (第93回, K-Z3 17時台帯初計測 run226A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 17:01:17–17:01:48 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 31.96 は production HTTP 実測のため gate 外 — rank 第93回 NEXT「K-Z3 17時台 n 積み増し」に従い 17時台を実施): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run226A 散発 3 件 (0.8815s 17番目 / 1.0668s 2番目 / 1.1094s 7番目) p50 59.1ms warm_p50 53.9ms / run226B 0/20 p50 63.7ms (max 184.4ms) / run226C 0/20 p50 50.2ms (max 144.4ms), control (kotobase.net/signup) cold 0/20 p50 94.7ms max 342.0ms 静穏で control 分離成立、cold 群は search 側に局在。run226A 散発 3 件は B/C 0/20 で即消失し run222A/223A 型「帯内 1 窓即消失」パターンと整合 (falsify 第96回 run225 の 15 分後の弱い再現)。17時台帯初計測で cold 3/60 (~5.0%) は 13–16時台低位帯 (5.0/3.3/2.2/2.0%) と同水準の再度低温帯サンプル — 日中低温帯分布パターン維持で traffic 依存説の方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。
## Iteration log"""

anchor = """本 tick は host load 32 の p50 上振れ (search p50 41–87ms, control p50 98ms) がみられるが cold 濃度判定 2/60 は閾値決定的。status 判定は rank に委ねる (rank 専門)。
## Iteration log"""

assert anchor in s, "anchor not found"
s = s.replace(anchor, ev, 1)
open(path, "w", encoding="utf-8").write(s)
print("inserted evidence OK")