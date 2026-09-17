#!/usr/bin/env python3
import io, sys
FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ANCHOR = "5 セット中位帯候補 (run385 採用可否は rank 判定に委ねる) — 17時台 (27/360 ~7.5%) と同水準の帯横断継続。status 判定は rank に委ねる (rank 専門)。"

ADD = " cosientist 2026-09-07 (第127回, K-Z3 18時台 n 積み増し run386A–C — bench 第170回 NEXT「委ねる; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し続行、次 run ID は run386 使用」の run386 枠, 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 18:54:31–18:54:39 JST, 全 80/80 200, host load1 8.23 (18:54 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run386A cold 単発 1/20 (1.2820s 散発配置, warm 群と交互) p50 56.8ms / run386B cold 0/20 p50 54.3ms / run386C cold 0/20 p50 50.1ms, control cold 0/20 p50 44.8ms 完全静穏で control 分離成立、cold 群は search 側に局在。run386A 単発は B/C 0/20 即消失し「帶内 1 窓即消失」散発単発型継続 (heavy>=6/20 は再達成せず)。18時台 (9/7) 通算 = run381 (2/60) + run382 (4/60) + run383 (7/60) + run384 (7/60) + run385 (2/60) + 本 tick run386 (1/60) = 23/360 (~6.4%) の 6 セット中位候補 — 17時台 (27/360 ~7.5%) と同水準の帯横断継続、日中帯 traffic 依存説の方向支持継続。status 判定は rank に委ねる (rank 専門)。qualify する新 evidence は 0 本 (K-Q1 は残余が cosientist 実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ — 実装は測定で qualify しない限り行わない (反証が先), K-Z2 は発火交互作用方向が非一貫で介入保留, K-S1/K-S2 は evidence なし) のため cosientist 実装対象なし — 観測 tick。"

with io.open(FN, "r", encoding="utf-8") as f:
    data = f.read()

if "run386A–C" in data:
    print("ALREADY_PRESENT")
    sys.exit(0)

if ANCHOR in data:
    data = data.replace(ANCHOR, ANCHOR + ADD, 1)
else:
    print("ANCHOR_NOT_FOUND")
    sys.exit(1)

with io.open(FN, "w", encoding="utf-8") as f:
    f.write(data)
print("DONE")