#!/usr/bin/env python3
import sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    data = f.read()

marker = "## Iteration log\n"
if marker not in data:
    print("ITER LOG HEADER NOT FOUND")
    sys.exit(1)

entry = "- 2026-09-08: bench 第187回。02:33 JST tick。HEAD 868b96d = cosientist 第130回 (02:08, run413 6/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; 本 tick 実測)。host load1 9.77 (02:33 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (bench 第186回, 02:12, run414 0/60)「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し続行、次 run ID は rank 判定待ち)」の続行枠。bench は 1 反復で K-Z3 2時台 (9/8) n 積み増し 1 セットを実施 (同一帯 independent)。run415 は sibling falsify/cosientist が 02:24 in-flight (.b415 02:24 作成) のため本測は run416 に読替 (run216/run256/run263 precedent, 同一帯 independent 計測として採用可否は rank 判定に委ねる)。K-Z3 2時台 run416A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 02:33:10–02:33:15 JST, 全 80/80 200, host load1 9.77 gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run416A cold 0/20 p50 0.0415s max 0.1360s / run416B cold 0/20 p50 0.0436s max 0.1349s / run416C cold 0/20 p50 0.0437s max 0.1466s, control (kotobase.net/signup) cold 0/20 p50 0.0394s max 0.1280s 完全静穏で control 分離成立 (search/control とも 0 cold)。run416 全 0/60 完全静穏は 2時台 (9/8) の完全静穏 2 セット目 (run414 0/60 → 本 tick run416 0/60 の深夜帯静穏 2 連続), 「帯内 1 窓即消失」散発単発/クラスタ型の非再現窓 (run413A 末尾集中 6/20 は 25 分後に完全静穏へ減衰, heavy>=6/20 は run413A 以降再達せず)。2時台 (9/8) 通算 = run413 (6/60) + run414 (0/60) + run416 (0/60) = 6/180 (~3.3%) の 3 セット中位〜低位帯候補 (run415 sibling in-flight は算入待ち) — 深夜最低帯 (traffic 最低) での健全静穏 2 連続中の cold 散発減衰終点 (run413A heavy 6/20 の 即減衰含む) は K-Z3 traffic 依存説への反証材料を継続 (9/7 深夜帯 ~2.5% 低位帯残界と整合方向, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し続行, 次 run ID は rank 判定待ち — ※sibling run415 は同一帯 independent 計測のため rank 判定の取込対象)。\n"

data = data.replace(marker, marker + entry, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(data)

print("ITER LOG ENTRY INSERTED")