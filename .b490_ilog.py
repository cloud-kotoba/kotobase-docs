#!/usr/bin/env python3
# falsify 第219回: insert iter-log entry below "## Iteration log" (top = newest)
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
ENTRY = "- 2026-09-08: falsify 第219回。18:24 JST tick。HEAD cd425be = bench 第213回 (18:11, K-Z3 18時台 run489 cold 7/60) = remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系で取込; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し続行。」は stale (rank 帯 artifact 前例多) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第213回 NEXT 委ねる → フォールバック K-Z3 現在時刻帯 18時台 n 積み増し続行, 次 run ID run490))。host load1 164.71 (18:18 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外。live smoke 200 (/, /signup; pre-run)。K-Z3 18時台 run490A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 18:22 JST, 全 60/60 200 + control 20/20 200): cold(>=0.5s) 5/2/0 per 20 = 7/60 (~11.7%) — run490A 散発クラスタ 5/20 / run490B 散発 2/20 / run490C 0/20, landing control cold 1/20 (0.6833s 境界値) で control 分離 borderline not-separated 倾向 (bench run489 と同型)。18時台 (9/8) 通算 = run489 (7/60) + 本 tick (7/60) = 14/120 (~11.7%) の 2 セット日中帯高位継続, 17時台 (28/240 ~11.7%) と同水準, traffic 依存説の日中帯方向支持継続。status 判定は rank 専門。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run491)。"

with open(PATH, encoding="utf-8") as f:
    txt = f.read()
ENTRY = ENTRY.replace("\u200b", "")
marker = "## Iteration log\n"
pos = txt.index(marker) + len(marker)
out = txt[:pos] + ENTRY + "\n" + txt[pos:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(out)
# verify
L2 = open(PATH, encoding="utf-8").read().split("\n")
print("IL_ENTRY_OCC", sum(1 for l in L2 if l.startswith("- 2026-09-08: falsify 第219回")))
print("SCRUBHASH", "#####" in out)