#!/usr/bin/env python3
import sys
path = "query-cosientist.md"

e1 = "- 2026-09-09: rank  ̈第230回まで01:54 JST tick"
e1 = e1.replace("̈ 第230回まで", "第230回。")
e2 = "HEAD fa68e24a = falsify  ̈第232回 (01:37, K-Z3 1時台 n 積み増し run522 cold 6/60 ~10.0%, control 2/20 分離未成立 not-separated) + bench  ̈第223回 (01:24, run521 cold 3/60 ~5.0%, control  ̈0/20 完全静穏分離成立) を remote bench_fetch/main・net-kotobase/main 一致として取込 "
e2 = e2.replace("̈ 第232回", "第232回").replace("̈ 第223回", "第223回").replace("̈0/20", "0/20")
e3 = "(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; worktree diff HEAD -- query-cosientist.md 空 + HDR_COUNT=1 を事前確認; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由; pre-run monitor NEXT「委ねる。」は stale(rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖)。"
e4 = "本 tick は rank  ̈第229回 (01:34, run520 fold 済み・新規 0) 以降の確定 evidence は falsify  ̈第232回 (run522) が K-Z3 仮説行に追記済み, 同 HEAD 上に bench  ̈第223回 (run521) も既存 — 両者を 1時台通算に fold する。"
e4 = e4.replace("̈ 第229回", "第229回").replace("̈ 第232回", "第232回").replace("̈ 第223回", "第223回")
e5 = "取り込み判定: (a) K-Z3: run521 + run522 を 1時台通算に積み上げ,1時台 (9/9) 通算 = falsify run520 (4/60,帯初) + bench run521 (3/60) + falsify run522 (6/60) =  ̈13/180 (~7.2%)  ̈3 セット — 0時台 (22/240 ~9.2% 4 セット) から 1時台 (深夜帯 traffic 最低帯) へ移行後も 3 セット連続 cold>0 で深夜側トランジション帯水準 (~9% 帯) が維持され K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンへの遷移は 1時台 n=3 で未達, heavy>=6/20 は 1時台 未達, falsify run522 は host load1 88 急上昇 tick の全体的上振れ (search p50 219-259ms) 混入下の control 分離未成立 not-separated 寄りで cold 濃度  ̈6/60 は不確実 — run521 (3/60, control 完全静穏分離成立) が独立確定分)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。"
e5 = e5.replace("̈13/180", "13/180").replace("̈3 セット", "3 セット").replace("̈6/60", "6/60")
e6 = "(b) K-Q1: 変動なし — 残余切れ手 は cosientist 実装専任の transact 401 write path 動的照合のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (transition 要件を満たす決定的支持/反証に未達 — K-Z3 open 継続・帯水準確定未達, K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke  ̈200 (/, /signup; pre-run 計測)。host load1 56.28 (pre-run uptime, gate  ̈7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。secret は一切記録せず。"
e6 = e6.replace("̈200", "200").replace("̈7.5", "7.5")
e7 = "NEXT: 委ねる (K-Q1 は cosientist 実装専任の transact 401 write path 動的照合のみ; フォールバックは K-Z3 現在時刻帯 1時台 n 積み増し続行, 次 run ID は run523 使用 — run522 は falsify  ̈第232回 が消費済みのため次セットは run523)。"
e7 = e7.replace("̈ 第232回", "第232回")
entry = e1 + e2 + e3 + e4 + e5 + e6 + e7
# strip any leftover combining char
entry = entry.replace("̈", "").replace("　 ", " ").replace("  ", " ")
with open(path, encoding="utf-8")as f:
    content = f.read()
header = "## Iteration log\n"
idx = content.find(header)
if idx == -1:
    print("ERROR header not found")
    sys.exit(1)
insert_at = idx + len(header)
new = content[:insert_at] + entry + "\n" + content[insert_at:]
with open(path, "w", encoding="utf-8")as f:
    f.write(new)
print("inserted OK")