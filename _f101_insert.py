#!/usr/bin/env python3
import io, sys

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

evidence = "falsify 2026-09-06 (第101回, K-Z3 18時台 n 積み増し run232A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 18:39:10–18:39:50 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 50–80 (18:33–18:38 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 — rank 第98回 NEXT「K-Z3 現在時刻帯 18時台 n 積み増し継続」に従い 18時台で実施; ※ run230/231 使用済みのため run232): cold(>=0.5s) 9/0/0 per 20 = 9/60 (~15%) — run232A heavy クラスタ 9/20 (0.958s/0.976s/1.067s/1.156s/1.542s/1.715s/1.793s/1.812s/2.307s — 冒頭 1–5 番目集中 + 8/10/17/19番目散発, p50 163.1ms max 2307.3ms) / run232B 0/20 p50 64.1ms max 155.3ms / run232C 0/20 p50 60.3ms max 89.0ms, control (kotobase.net/signup) cold 0/20 p50 60.0ms max 108.6ms 完全静穏で control 分離成立、cold 群は search 側に局在。run232A の 9/20 heavy cold クラスタは「帯内 1 窓即消失」パターン (従来 1–4/60) を大幅に超える規模で B/C 0/20 により単一窓即消失 — 18時台通算 (run230 1/60 + run231 3/60 + 本 tick 9/60) で 13/180 (~7.2%) に跳ね上がり、18時台「低位帯候補」(4/120 ~3.3%) は本 tick 単一窓で重く上振れ (帯内散発ではなく単一窓 heavy burst)。control 分離成立 (control 0/20) なので search 側実在 cold で worker cold-start / scale-from-zero 型の単発イベントと整合 — 深夜帯 ~26-31% 平坦パターンまでの時間帯非依存の突発 cold 出現は traffic 依存説に弱い反証方向 (時間帯判別性が揺らぐが n=1 イベントで決定的反証ではない)。status 判定は rank に委ねる (rank 専門)。"

anchor = "\n## Iteration log"

doc = open(P, encoding="utf-8").read()
cnt = doc.count(anchor)
print("anchor_count=", cnt)

if cnt != 1:
    print("ABORT: anchor count != 1")
    sys.exit(1)

ins = "\n" + evidence
newdoc = doc.replace(anchor, ins + anchor)

# verify
print("evidence_occurrences_after:", newdoc.count("第101回"))
open(P, "w", encoding="utf-8").write(newdoc)
print("WROTE_OK")