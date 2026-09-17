#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

anchor = "14時台は帯初サンプル 4/60 (~6.7%, 9/5 run152 5/60 と同水準)。status 判定は rank に委ねる (rank 専門)。"

assert txt.count(anchor) == 1, "anchor count = %d" % txt.count(anchor)

addition = (" falsify 2026-09-06 (第88回, K-Z3 14時台 n 積み増し run213A–C, 同測定法 n=20 × 3 + "
"landing control, 別接続 curl, Tokyo, 14:43–14:44 JST 14:43:59–14:44:27, 全 80/80 200, host load1 16.25 は "
"production HTTP 実測のため gate 外): run213A cold(>=0.5s) 4/20 (0.989/1.007/0.921/1.048s — 散発配置 1/5/11/18番目, "
"warm 群 p50 61.8ms) / run213B cold 0/20 p50 39.1ms (max 70.4ms) / run213C cold 0/20 p50 59.0ms (max 173.9ms) — "
"landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 53.0ms max 262.7ms と静穏で "
"control 分離成立、cold 群は search 側に局在。run213A 散発 4 件は run212A 冒頭集中型ではなく帯内散発型だが "
"B/C 0/20 で即消失し「帯内 1 窓即消失」パターンと整合 (run212A 型の弱い再現)。14時台通算は run212 (4/60) + "
"run211 (1/60) + run213 (4/60) で 9/180 (~5.0%) の低位帯残界 — 9/5 run152 5/60 と合算すると 14/240 ~5.8%, "
"低位帯分布 (7時台 ~2.2% < 14時台 ~5.8% < 11時台 7.5-13% < 16時台 ~15%) パターンに整合し traffic 依存説の方向を支持継続、"
"深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。")

# insert after anchor (the run212 entry tail) and before the next newline
idx = txt.index(anchor) + len(anchor)
txt = txt[:idx] + addition + txt[idx:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)
print("inserted ok")