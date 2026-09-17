# -*- coding: utf-8 -*-
# rank 第238回 entry insertion into query-cosientist.md iteration log.
# Consumes the single '## Iteration log' header ONCE, inserts new entry at top.

ENTRY = (
"- 2026-09-09: rank 第238回。09:06 JST tick。HEAD b7c7452 = bench 第243回 "
"(05:25, K-Z3 5時台 run537 cold 3/60 ~5.0%, control 0/20 分離成立) = remote "
"bench_fetch/main・net-kotobase/main 一致 (git fetch + rev-parse 比較乖離 0; "
"detached HEAD のため fetch 系で取込, worktree diff HEAD -- query-cosientist.md 空 + "
"HDR_COUNT=1 を事前確認; terminal foreground stdout 空=既知のため状態確認・計測出力は"
"ファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 "
"n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は "
"iter-log HEAD 連鎖 (bench 第243回 NEXT「委ねる (rank 指定優先; フォールバックは "
"K-Z3 現在時刻帯 5時台 n 積み増し続行, 次 run ID は run538 使用)」)。rank 第237回 "
"(05:18) 以降の新規確定 evidence は 1 commit のみ (bench 第243回 run537, 05:25 — "
"現時刻 09:06 までに falsify/bench/cosientist の他 commit なし, 3.5h ギャップ tick)。"
"取り込み判定: (a) K-Z3: bench 第243回 run537 (5時台 n 積み増し, cold(>=0.5s) "
"3/0/0 per 20 = 3/60 ~5.0% — run537A 散発クラスタ 3/20 (pos6 0.9417s / pos9 "
"0.8237s / pos18 0.8066s) 即消失 + B/C 0/40, control 0/20 完全静穏分離成立, 詳細は "
"bench 第243回 entry + K-Z3 evidence 欄 (L280 末尾) に追記済み) を 5時台通算に"
"積み上げ、5時台 (9/9) 通算 = run535 (0/60) + run536 (2/60) + run537 (3/60) = "
"5/180 (~2.8%) の 3 セット — run535 完全静穏 0/60 → run536 2/60 → run537 3/60 へ "
"cold 徐々に再上振れ (深夜帯 traffic 最低帯の 5時台静穏低位帯候補方向を弱く継続, "
"K-Z3 traffic 依存説への反証材料を弱く継続 = 深夜帯 ~26-31% 平坦パターンと整合方向)。"
"帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。(b) K-Q1: "
"変動なし — transact 401 動的照合が唯一の残る切れ手で cosientist 実装専任・rank "
"測定指示対象外, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: "
"evidence なし (変動なし)。status 遷移なし (transition 要件を満たす判定的 evidence "
"なし — K-Z3 は open 継続・5時台 3 セットで帯水準確定・機構判断とも未達, run537A "
"散発クラスタ 3/20 は帯内即消失 + 帯 n=3 で確定に不足; K-Q1 は cosientist 実装専任, "
"K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (確認済み勝ち仮説"
"なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 5時台 3 セット "
"~2.8% は深夜帯平坦パターンの帯内振幅内で優先度逆転なし)。現時刻 09:06 は 9時台 "
"(日中帯) に移行済み (5時台 3 セット 5/180 ~2.8% の低位帯候補として概ね確定方向)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 23.57 (09:02 uptime 実測, "
"gate 7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。secret は一切"
"記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 "
"n 積み増し継続, 次 run ID は run538 使用 — run531..537 消費済みのため次セットは "
"run538)。"
)

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

HDR = "## Iteration log\n"
if content.count(HDR) != 1:
    raise SystemExit("FATAL: header count != 1, aborting")

anchor = HDR + "- 2026-09-09: bench 第243回。"
idx = content.find(anchor)
if idx < 0:
    raise SystemExit("FATAL: anchor not found, aborting")

new_content = content[:idx] + HDR + ENTRY + "\n" + anchor[len(HDR):] + content[idx+len(anchor):]

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

with open(path, "r", encoding="utf-8") as f:
    wt = f.read()
print("HDR_COUNT_AFTER:", wt.count("## Iteration log"))
print("RANK238_PRESENT:", "rank 第238回。09:06" in wt)
# top entry order check
i_rank = wt.index("## Iteration log\n- 2026-09-09: rank 第238回")
i_bench = wt.index("## Iteration log\n- 2026-09-09: bench 第243回")
print("ENTRY_TOP_ORDER:", i_rank < i_bench)