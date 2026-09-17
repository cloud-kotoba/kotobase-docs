#!/usr/bin/env python3
# rank 第225回 iter-log entry insert into query-cosientist.md
import io, sys

FN = 'query-cosientist.md'
ENTRY = (
"- 2026-09-09: rank 第225回。00:37 JST tick。HEAD b8d4b5f = bench 第228回 (00:04, K-Z3 0時台 n-add run517 cold 6/60 ~10.0%; parent falsify 第229回 00:16 run516 cold 5/60 ~8.3%) を remote bench_fetch/main・net-kotobase/main 一致として取込 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; worktree diff HEAD -- query-cosientist.md は空 クリーン + HDR_COUNT=1 を事前確認; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (falsify 第229回 NEXT「次 run ID は run517」で falsify run516 → bench run517 まで達した枠))。rank 第224回 (50870c7, 23:59) 以降の新規確定 evidence は 2 commit、ともに K-Z3 0時台: (a) falsify 第229回 (8676b70, run516, 00:15, 0時台 n 積み増し): cold 5/0/0 per 20 = 5/60 (~8.3%) — run516A 中盤集中クラスタ 5/20 (pos4 2.0083s + pos7-10 連続 4 件 1.3814/1.4217/1.7193/2.3828s) p50 281.9ms, B/C 0/40, control 0/20 完全静穏で control 分離成立, cold 群 search 側局在。(b) bench 第228回 (b8d4b5f, run517, 00:04, 0時台 n 積み増し): cold 6/60 (~10.0%) — run517A 散発クラスタ 4/20 + run517B 散発 2/20 + run517C 0/20, control 0/20 完全静穏分離成立, cold 群 search 側局在。取り込み判定: (a) K-Z3: run516 + run517 を 0時台 (24時台) 通算に積み上げ、0時台 通算 = run516 (5/60) + run517 (6/60) = 11/120 (~9.2%) 2 セット — 23時台 (23/240 ~9.6%) から 0時台 へ移行後も cold 多発クラスタ継続 (深夜帯 traffic 最低帯 0時台での cold 多発クラスタは K-Z3 traffic 依存説への反証材料継続, heavy>=6/20 は run517A (4/20) で持続せず「帯内 1 窓即消失」型継続, 深夜帯 ~26-31% 平坦パターンへの遷移は帯通算 n=2 で未達)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。(b) K-Q1: 変動なし — 残余切れ手 は cosientist 実装専任の transact 401 write path 動的照合のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (transition 要件を満たす決定的支持/反証に未達 — K-Z3 open 継続・帯水準確定未達, K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run 計測)。host load1 ~36 (pre-run uptime, gate 7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。secret は一切記録せず。NEXT: 委ねる (K-Q1 は cosientist 実装専任の transact 401 write path 動的照合のみ; フォールバックは K-Z3 現在時刻帯 0時台 n 積み増し続行, 次 run ID は run518 使用)。"
)

with io.open(FN, encoding='utf-8') as f:
    text = f.read()

HEADER = '## Iteration log\n'
i = text.index(HEADER)
nl = text.index('\n', i + len(HEADER))
new_text = text[:i] + HEADER + ENTRY + '\n' + text[i + len(HEADER):]

if new_text.count(HEADER) != 1:
    print("ERROR header count != 1"); sys.exit(1)

with io.open(FN, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("OK inserted; total_lines=", new_text.count('\n')+1)