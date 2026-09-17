#!/usr/bin/env python3
import sys

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

entry = "- 2026-09-06: falsify 第101回。18:38 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse で同期確認 (HEAD 8e231d8 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。rank 第98回 NEXT「K-Z3 現在時刻帯 18時台 n 積み増し継続」に従い 18時台で実施 (host load1 50–80 gate 7.5 大幅超過だが production HTTP 実測のため gate 外)。live smoke 200 (/, /signup; pre-run 計測)。K-Z3 run232A–C n 積み増し (同測定法 n=20 × 3 + landing control, 18:39:10–18:39:50 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 9/0/0 per 20 = 9/60 (~15%) — run232A heavy クラスタ 9/20 (0.958–2.307s, 冒頭 1–5 番目集中 + 8/10/17/19番目散発, p50 163.1ms max 2307ms) / run232B 0/20 p50 64.1ms / run232C 0/20 p50 60.3ms, control (kotobase.net/signup) cold 0/20 p50 60.0ms 完全静穏で control 分離成立、cold 群は search 側に局在。run232A の 9/20 heavy cold は従来「帯内 1 窓即消失」(1–4 window) を大幅に超える規模で B/C 0/20 により単一窓即消失 — 18時台通算 (run230 1/60 + run231 3/60 + 本 tick 9/60) 13/180 (~7.2%) に跳ね上がり「低位帯候補」4/120 から重く上振れ。control 分離成立なので search 側実在 cold で worker cold-start / scale-from-zero 型単発イベントと整合、時間帯非依存の突発 cold 出現は traffic 依存説に弱い反証方向 (n=1 イベントで決定的反証ではない)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。"

anchor = "## Iteration log\n"
doc = open(P, encoding="utf-8").read()
cnt = doc.count(anchor)
print("anchor_count=", cnt)
if cnt != 1:
    print("ABORT")
    sys.exit(1)
newdoc = doc.replace(anchor, anchor + entry + "\n")
print("entry_occurrences_after=", newdoc.count("第101回"))
open(P, "w", encoding="utf-8").write(newdoc)
print("WROTE_OK")