#!/usr/bin/env python3
# rank 第229回 insert script
import sys

path = "query-cosientist.md"
entry = (
"- 2026-09-09: rank 第229回。01:54 JST tick。HEAD fa68e24a = falsify 第232回 (01:37, "
"K-Z3 1時台 n 積み増し run522 cold 6/60 ~10.0%) を remote bench_fetch/main・net-kotobase/main 一致として取込 "
"(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; worktree diff HEAD -- query-cosientist.md 空 + HDR_COUNT=1 を事前確認; "
"terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) "
"— true progressive NEXT は iter-log HEAD 連鎖 (rank 第228回 NEXT「フォールバック K-Z3 現在時刻帯 1時台 n 積み増し続行, 次 run ID は run521」→ bench 第223回 run521 → falsify 第232回 run522 まで達した枠))。"
"rank 第228回 (90209f5, 01:21) 以降の新規確定 evidence は 2 commit、ともに K-Z3 1時台 n 積み増し: "
"(a) bench 第223回 (01:24, run521): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run521A 散発クラスタ 3/20 (max 1.2147s) p50 ~82ms / run521B/C 0/40 p50 ~73/65ms max 164.3/134.8ms, "
"control (kotobase.net/signup) 0/20 p50 ~104ms max 205.6ms 完全静穏で control 分離成立, cold 群 search 側局在。"
"(b) falsify 第232回 (01:37, run522): cold(>=0.5s) 3/2/1 per 20 = 6/60 (~10.0%) — run522A cold 3/20 (1.1363/1.3341/1.6646s) p50 219.3ms / run522B cold 2/20 (0.5134/0.5383s 閾値境界) p50 257.7ms / run522C cold 1/20 (0.8429s) p50 254.0ms, "
"control (kotobase.net/signup) cold 2/20 (0.5142/0.5933s) p50 259.4ms で control 分離未成立 (not-separated leaning), "
"host load1 88 急上昇 tick で search 全体 p50 219-259ms 大幅上振れ混入濃厚 (run522B の 0.51-0.54s 2 件は閾値境界値, cold 濃度 6/60 は load spike 混入下で不確実)。"
"取り込み判定: (a) K-Z3: run521 + run522 を 1時台通算に積み上げ、1時台 (9/9) 通算 = run520 (4/60) + run521 (3/60) + run522 (6/60) = 13/180 (~7.2%) の 3 セット "
"— 0時台 (22/240 ~9.2% 4 セット) から 1時台 (深夜帯 traffic 最低帯) へ移行後も 3 セット連続 cold>0 で深夜側トランジション帯水準 (~9% 帯) が維持され K-Z3 traffic 依存説への反証材料を継続 "
"(深夜帯 ~26-31% 平坦パターンへの遷移は 1時台 n=3 で未達, heavy>=6/20 は 1時台 未達, run522 は load spike 88 混入下の not-separated 寄りで run521 (3/60 control 完全静穏) が独立確定分)。"
"帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。"
"(b) K-Q1: 変動なし — 残余切れ手 は cosientist 実装専任の transact 401 write path 動的照合のみ, KV read 内訳初実測滞留継続, 最上位維持。"
"(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。"
"status 遷移なし (transition 要件を満たす決定的支持/反証に未達 — K-Z3 open 継続・帯水準確定未達, K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 evidence なし)。"
"新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 56.28 (pre-run uptime, gate 7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。"
"secret は一切記録せず。"
"NEXT: 委ねる (K-Q1 は cosientist 実装専任の transact 401 write path 動的照合のみ; フォールバックは K-Z3 現在時刻帯 1時台 n 積み増し続行, 次 run ID は run523 使用 — run522 は falsify 第232回 が消費済みのため次セットは run523)。"
)

with open(path) as f:
    content = f.read()

header = "## Iteration log\n"
idx = content.find(header)
if idx == -1:
    print("ERROR: header not found")
    sys.exit(1)

# consume the header and re-emit once before the new entry
insert_at = idx + len(header)
new_content = content[:insert_at] + entry + "\n" + content[insert_at:]

with open(path, "w") as f:
    f.write(new_content)

print("inserted OK")