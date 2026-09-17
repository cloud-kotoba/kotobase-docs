#!/usr/bin/env python3
import sys

PATH = 'query-cosientist.md'
ANCHOR = "bench 2026-09-07 (第118回, K-Z3 2時台(深夜帯) n 積み増し run289A–C"

INS = " falsify 2026-09-07 (第132回, K-Z3 2時台(深夜帯) n 積み増し run290A–C — bench 第118回 (02:40, run289) に続く 2時台 n 積み増し (次 run ID run290), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 02:46:28–02:46:35 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 30.22 (02:46 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run290A cold 単発散発 1.3134s (15番目 散発) p50 0.0498s max 1.313s warm 群 0.041–0.088s / run290B cold 0/20 p50 0.0490s max 0.120s / run290C cold 0/20 p50 0.0451s max 0.053s, control (kotobase.net/signup) cold 0/20 p50 0.0426s max 0.054s 完全静穏で control 分離成立、cold 群は search 側に局在。run290A 単発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (bench run289A-C 完全静穏 0/60 の直後の 1 件再出現、heavy クラスタは run271A 以降 17 セット非再現)。2時台通算 run284 (1/60) + bench run285 (3/60) + falsify run286 (1/60) + bench run287 (1/60) + falsify run288 (1/60) + bench run289 (0/60) + 本 tick (1/60) = 8/420 (~1.9%) の 7 セット、deep-night 累計 run275..290 = 21/960 (~2.2%) の 16 セットで低位帯水準継続 — 深夜最低帯での cold 散発再出現 (run289 完全静穏 1 セット + run283 完全静穏 を挟み) は K-Z3 traffic 依存説への反証材料を継続。ただし control 分離成立・cold 1/60 薄散発で機構判定には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。\n"

with open(PATH) as f:
    lines = f.readlines()

idx = None
for i, l in enumerate(lines):
    if l.startswith(ANCHOR):
        idx = i
        break

if idx is None:
    print("ANCHOR NOT FOUND", file=sys.stderr)
    sys.exit(1)

lines[idx] += INS
with open(PATH, 'w') as f:
    f.writelines(lines)
print("inserted after line", idx)