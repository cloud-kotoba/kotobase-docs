#!/usr/bin/env python3
import sys, io

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Verify exactly one Iteration log header
hdr = content.count("## Iteration log")
if hdr != 1:
    sys.stderr.write("FATAL: header count = %d (expected 1), abort\n" % hdr)
    sys.exit(2)

anchor = "## Iteration log\n- 2026-09-08: falsify 第216回。"
if anchor not in content:
    sys.stderr.write("FATAL: anchor not found, abort\n")
    sys.exit(2)
if content.count(anchor) != 1:
    sys.stderr.write("FATAL: anchor count = %d (expected 1), abort\n" % content.count(anchor))
    sys.exit(2)

entry = ("- 2026-09-08: rank 第214回。16:52 JST tick。HEAD 72db7f1 = falsify 第216回 "
         "(16:49, K-Z3 16時台 n-add run483 cold 5/60 ~8.3% — run483A 散発 2/20 + run483C 薄 3/20, "
         "control 0/20 静穏分離成立; 並行 cosientist run482 編集と同居 commit, 前 HEAD 9807184 = bench 第209回 run481) "
         "= remote bench_fetch/main・net-kotobase/main 一致 (fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため "
         "fetch 系で取込; worktree diff HEAD -- query-cosientist.md は空 (クリーン)+HDR_COUNT=1 を事前確認; "
         "※本 tick 開始時に sibling cosientist 第144回 (run482) の uncommitted 編集 (HEAD 9807184 時点, iter-log 行) を検知し"
         "挿入・上書きせず ~85s 待機+再 fetch で falsify 第216回 commit (72db7f1, run483 + 同居 run482) 着弾・HEAD 前進・"
         "diff empty 化を確認の上 72db7f1 上へ単一 rank 行のみ挿入, header=1 事前確認済; terminal foreground stdout 空=既知のため"
         "状態確認はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale "
         "(rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (falsify 第216回「委ねる, 次 run ID run484」))。"
         "rank 第213回 (7b90d45, 16:17) 以降の新規確定 evidence は 3 commit・4 run セット、すべて K-Z3 16時台 n-add: "
         "(a) falsify 第215回 commit (01be140, run480): cold 5/60 ~8.3% — run480A 散発クラスタ 5/20 (0.8955-2.0793s), "
         "B/C 0/40, control 0/20 静穏分離成立。"
         "(b) bench 第209回 commit (9807184, run481): cold 3/60 ~5.0% — run481A 3/20, B/C 0/40, control 0/20 静穏分離成立。"
         "(c) cosientist 第144回 run482 (72db7f1 に同居 bundling): cold 6/60 ~10.0% — run482A 散発クラスタ 5/20 + B 単発 1/20, "
         "control 0/20 静穏分離成立。"
         "(d) falsify 第216回 commit (72db7f1, run483): cold 5/60 ~8.3% — run483A 散発 2/20 + run483C 薄 3/20, "
         "control 0/20 静穏分離成立。"
         "取り込み判定: (a) K-Z3: run480-483 を 16時台通算に積み上げ、16時台 (9/8) 通算 = run479 (6/60, 帯初) + run480 (5/60) "
         "+ run481 (3/60) + run482 (6/60) + run483 (5/60) = 25/300 (~8.3%) の 5 セット中〜高位帯候補。"
         "帯初再上振れ (run479 6/60) → 帯内散発減衰 (5/60 → 3/60) → 再上振れ (6/60 → 5/60) の日中帯 high 側パターン継続、"
         "14時台 (22/300 ~7.3% 5セット)・15時台 (21/240 ~8.8% 4セット) と同水準の中位帯継続、traffic 依存説の日中帯方向支持継続、"
         "深夜帯 ~26-31% 平坦パターンとの対比不変。heavy>=6/20 は 16時台で未達 (run479A/480A/482A 散発クラスタ 5/20 級のみで"
         "帯水準として持続せず「帯内 1 窓即消失」散発型継続)。帯 n=5 セットで帯水準確定・機構判断には未達 (中位帯候補のまま)。"
         "(b) K-Q1: 変動なし (残余切れ手は cosientist 実装専任の動的照合のみ, KV read 内訳初実測滞留継続, 最上位維持)。"
         "(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。"
         "status 遷移なし (transition 要件を満たす決定的支持/反証に未達 — K-Z3 open 継続・帯水準確定未達, K-Q1 は cosientist "
         "実装専任, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。"
         "rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run 計測)。"
         "host load1 63.97 (16:49 pre-run uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本更新のみで影響なし。"
         "secret は一切記録せず。NEXT: K-Z3 現在時刻帯 16時台 n 積み増し続行 (次 run ID run484 — 16時台 25/300 ~8.3% "
         "5セットで帯水準確定未達, falsify/bench が実施)。\n")

new = content.replace(anchor, "## Iteration log\n" + entry + "- 2026-09-08: falsify 第216回。")

if new.count("## Iteration log") != 1:
    sys.stderr.write("FATAL: post-insert header count = %d, abort\n" % new.count("## Iteration log"))
    sys.exit(2)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(new)

sys.stdout.write("INSERT_OK header=%d\n" % new.count("## Iteration log"))