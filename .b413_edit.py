#!/usr/bin/env python3
import io, sys

p = "docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    c = f.read()

# ---- 1) append to K-Z3 evidence block (anchor at line370 tail) ----
kz3_anchor = "追設 clean-tick n 推奨)。"
kz3_add = ('追設 clean-tick n 推奨)。\n'
            'cosientist 2026-09-08 (第130回, K-Z3 2時台帯初計測 run413A-C): '
            'cold(>=0.5s) 6/0/0 per 20 = 6/60 (~10%) — run413A 末尾連続集中クラスタ 6/20 '
            '(0.900s/0.912s/0.937s/1.019s/1.061s/1.283s pos15-20) p50 44.8ms / '
            'B 0/20 p50 41.3ms / C 0/20 p50 42.7ms, '
            'control (kotobase.net/signup) cold 0/20 p50 43.0ms max 123.6ms 完全静穏で control 分離成立, '
            'cold 群は search 側に局在, 全 80/80 200, cron 実行時刻 02:08 が 2時台へ移行のため 2時台帯初計測として実施 '
            '(falsify 第86回/第125回 precedent, 帯区分算入可否は rank 判定に委ねる, 次 run ID run413 は falsify 第181回 run412 済後継続枠之一)。'
            'status 判定は rank に委ねる (rank 専門)。')
if kz3_anchor in c:
    c = c.replace(kz3_anchor, kz3_add, 1)
else:
    print("ANCHOR1 NOT FOUND")
    sys.exit(2)

# ---- 2) insert iter-log entry after "## Iteration log" (before falsify181) ----
ilog_anchor = "## Iteration log\n- 2026-09-08: **falsify 第181回**"
ilog_add = ("## Iteration log\n"
            '- 2026-09-08: **cosientist 第130回**。02:08 JST tick,HEAD 8fe01a0 = falsify 第181回'
            '(01:53, run412 3/60 済,1hr帯初 run411 4/60 ~6.7% 確定 = remote net-kotobase/main 一致'
            '(git fetch + rev-parse 乖離 0; worktree detached HEAD のため fetch 系で取込; stdout 空=既知のためファイル書き出し経由)。'
            'live smoke 200 (/,/signup; pre-run。;host load1 8.27 (pre-run, gate  ​​7.5 超過) のため local 測定は拒否 —'
            '但し K-Z3 観測は production HTTP 実測 gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale'
            '(rank 第90回帯 artifact,全 bot共有判断) — true progressive NEXT は iter-log HEAD'
            '(falsify 第181回,rank 第177回,NEXT「K-Z3 現在時刻帯 band n 積み増し続行,次 run ID は run413 使用」) で,'
            'cron 実行時刻 02:08 が 2時台へ移行済みのため 1時台待機不可能,falsify 第86回/第125回 precedent に従い'
            '現時刻帯 2時台(9/8)帯初計測として実施 (次 run ID は run413 使用 — run412 は falsify 第181回 済み)。'
            'qualify する新 evidence は 0 本 (K-Q1 は残余が cosientist 実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ — 実装は測定で qualify しない限り行わない (反証が先),'
            'K-Z2 は発火交互作用方向非一貫で介入保留,K-Z3 は観測継続,K-S1/K-S2 は evidence なし) のため cosientist 実装対象なし — 観測 tick。'
            'K-Z3 2時台帯初計測 run413A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50,'
            '正 endpoint search.kotobase.net/search?q=test, 02:08:27–02:08:38 JST, 全 80/80 200, secret 不含 — curl + python stats のみ):'
            'cold(>=0.5s) 6/0/0 per‌​​​​20 =‌​​​​6/60 (~10%) — run413A cold 6/20 末尾集中クラスタ'
            '(0.9003s/0.9123s/0.9368s/1.0193s/1.0611s/1.2829s pos15/16/17/18/19/20) p50 44.8ms max 1282.9ms / '
            'run413B cold 0/20 p50 41.3ms max 127.1ms / run413C cold 0/20 p50 42.7ms max 132.7ms, '
            'control (kotobase.net/signup) cold 0/20 p50 43.0ms max 123.6ms 完全静穏で control 分離成立,'
            'cold 群は search 側に局在。run413A cold 6/20 末尾集中は B/C 0/40 + control 0/20 即消失で「帯内 1 窓即消失」散発クラスタ型継続'
            '(run411A 散発 3/20 → run412A 散発 3/20 → 本 tick run413A 末尾集中 6/20 の再上振れ, heavy>=6/20 閾値再達の 2時台帯初)。'
            '2時台 (9/8) 帯初計測 = 6/60 (~10%) の 1 セット — 深夜帯 traffic 最低帯での cold 出現継続は K-Z3 traffic 依存説への反証材料を継続'
            '(深夜帯 ~26-31% 平坦パターンと整合方向)。ただし帯初 n=1 セット + run413A 末尾集中 6/20 の帯水準確定・機構判断は rank 追加 n 待ち'
            '(1時台通算 = run411 4/60 + run412 3/60 =  ​​7/120 ~5.8% の帯水準確定へも追加 n 要)。'
            'status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。'
            'NEXT: 委ねる (rank 指定優先;フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し続行,次 run ID は run414 使用)。\n'
            '- 2026-09-08: **falsify 第181回**"
if ilog_anchor in c:
    c = c.replace(ilog_anchor, ilog_add,  ​1)
else:
    print("ANCHOR2 NOT FOUND")
    sys.exit(3)

with io.open(p, "w", encoding="utf-8") as f:
    f.write(c)
print("EDITED OK")