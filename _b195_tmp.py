#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")

ev = " bench 2026-09-08 (第195回, K-Z3 8時台帯内 4セット目 n 積み増し run441A–C — rank 第193回 NEXT の run440 枠は falsify 第195回 (8時台帯内 3セット目, cold 2/60) が先行使用のため run441 に読替 (run216/run256/run263/run278 precedent, 同一帯 independent 2計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 08:24–08:29 JST, 全 80/80 200, host load1 13.5–18.0 (08:23→08:29 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/0/0 per 20 =  ̈1/60 (~1.7%) — run441A 単発 1.4515s (p50 51.7ms warm_p50 51.7ms) / run441B cold 0/20 p50 46.6ms max 134.9ms / run441C cold 0/20 p50 42.2ms max 145.6ms, control (kotobase.net/signup) cold 0/20 p50 42.8ms max 128.7ms 完全静穏で control 分離成立,cold 群は search 側に局在。run441A 単発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (falsify-run440A/B 各単発 に対する独立計測の弱い再現, heavy>=6/20 は run413A 以降非再現継続)。8時台 (9/8) 通算 = bench-run437 (cold 2/60,帯初) + falsify-run438 (cold 1/60) + falsify-run440 (cold 2/60) +本 tick run441 (cold 1/60) =  ̈6/240 (~2.5%) の 4 セット低位帯継続 — 5/6時台 完全静穏 と 7時台 8/360 ~2.2% に続く朝帯境低位帯の遷移継続で 深夜帯→朝帯境静穏方向に整合, 23時台前回帯 (~5.2%) と深夜帯 ~26-31% 平坦パターンとの対比は traffic 依存説の方向支持を維持。status 判定は rank に委ねる (rank 専門)。"

idx = None
for i, ln in enumerate(lines):    # <-- needs closing paren
    if ln.startswith("| K-Z3 "):
        idx = i  # noqa: E702
        break
    print()  # placeholders removed below
X