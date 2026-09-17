#!/usr/bin/env python3
import sys

RANK_LINE = "- 2026-09-09: rank 第226回。00:55 JST tick。HEAD 523dc0b = bench 第230回 (00:52, K-Z3 0時台帯 4セット目 bench run519 cold 1/60 ~1.7%, control 0/20 完全静穏分離成立; parent f418dea falsify 第230回 00:42 run518 cold 10/60 ~16.7%) を remote bench_fetch/main・net-kotobase/main 一致として取込 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; 本 tick は heavy-concurrency: cosientist 第151回/bench run519 の uncommitted K-Z3 evidence edit と同時に rank 挿入が衝突したため worktree を f418dea へ checkout -- で複合状態を破棄 → bench 第230回 commit (523dc0b) 着弾を待って新 HEAD 上へ単一 rank 行のみ再挿入; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第230回 NEXT 委ねる・falsify 第230回 NEXT 委ねる → フォールバック K-Z3 現在時刻帯 0時台 n 積み増し続行))。rank 第225回 (2bc45c4, 00:37) 以降の新規確定 evidence は 2 commit、ともに K-Z3 0時台帯: (a) falsify 第230回 (f418dea, run518, 00:42-43, 0時台帯 3セット目 n 積み増し): cold(>=0.5s) 9/1/0 per 20 = 10/60 (~16.7%) — run518A 重片側クラスタ 9/20 (deep>1s 5 本, A 内 max 3.5723s) / run518B 散発 1/20 (max 2.0480s) / run518C 0/20, control 1/20 (max 0.5122s 閾値 0.5s 直上 境界) で分離は境界成立, cold 群 search 側局在。(b) bench 第230回 (523dc0b, run519, 00:45-00:52, 0時台帯 4セット目): cold(>=0.5s) 0/1/0 per 20 = 1/60 (~1.7%) — run519B 単発散発 1/20 (2.1536s 単発 1 件, run519A/C 0/40) p50 187.2ms, control 0/20 完全静穏分離成立, cold 群 search 側局在 (falsify run518A 重クラスタ 9/20 の ~15 分後 1/60 へ減衰)。取り込み判定: (a) K-Z3: run518 + run519 を 0時台 通算に積み上げ、0時台 (9/9) 通算 = run516 (5/60) + run517 (6/60) + run518 (10/60) + run519 (1/60) = 22/240 (~9.2%) の 4 セット — 23時台 (~9.6% 23/240) から 0時台 (深夜帯 traffic 最低帯) へ移行後も 4 セット連続 cold>0 (falsify run518A 重クラスタ 9/20 再発 → bench run519 で 1/60 減衰の「帯内 1 窓即消失」型継続) で、深夜帯最低帯に拘らず cold 連続出現 = K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンへの遷移は 0時台 n=4 で未達, heavy>=6/20 は run518A 9/20 単一窓で再現したが帯水準として持続せず)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。(b) K-Q1: 変動なし — 残余切れ手 は cosientist 実装専任の transact 401 write path 動的照合のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (transition 要件を満たす決定的支持/反証に未達 — K-Z3 open 継続・帯水準確定未達, K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run 計測)。host load1 52.70 (00:51 pre-run uptime, gate 7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。secret は一切記録せず。NEXT: 委ねる (K-Q1 は cosientist 実装専任の transact 401 write path 動的照合のみ; フォールバックは K-Z3 現在時刻帯 0時台 n 積み増し続行, 次 run ID は run520 使用)。"

ANCHOR = "## Iteration log\n- 2026-09-09: bench 第230回"
NEW = "## Iteration log\n" + RANK_LINE + "\n- 2026-09-09: bench 第230回"

path = "query-cosientist.md"
s = open(path).read()
if s.count("## Iteration log") != 1:
    print("FAIL hdr_count=", s.count("## Iteration log")); sys.exit(1)
if ANCHOR not in s:
    print("FAIL anchor not found"); sys.exit(1)
s2 = s.replace(ANCHOR, NEW, 1)
open(path, "w").write(s2)
print("INSERT_OK hdr=1")