# -*- coding: utf-8 -*-
path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(path, encoding='utf-8') as f:
    content = f.read()

entry = "- 2026-09-08: rank 第209回。13:40 JST tick。HEAD 5f15ac6 = bench 第193回 (13:30, K-Z3 13時台帯初計測 run467 cold 8/60 ~13.3% heavy 寄り — run467A 8/20 冒頭4連続+散発, control 完全静穏分離成立) = remote bench_fetch/main・net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; worktree diff HEAD -- query-cosientist.md は空 (クリーン)+HDR_COUNT=1 を事前確認; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖)。rank 第208回 (9532f63, 13:26) 以降の新規確定 evidence は 1 commit: bench 第193回 (5f15ac6, 13:30) の run467 (13時台帯初計測, 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 13:24–13:25 JST, 全 80/80 200, host load1 106.79 (13:24 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外): cold 8/0/0 per 20 = 8/60 (~13.3%) — run467A heavy 寄り散発クラスタ 8/20 (1.19–1.91s, 冒頭 4 連続 + 中盤以降散発 4 件), B/C 0/40 即消失, control 0/20 (kotobase.net/signup) 完全静穏で control 分離成立。取り込み判定: (a) K-Z3: run467 を 13時台 (9/8) 帯初計測として取込 — 13時台 (9/8) 通算 = run467 (8/60, 帯初) = 8/60 (~13.3%) の 1 セット heavy 寄り帯初クラスタ。12時台帯初 (run462 8/60 ~13.3%) と同水準の帯初再上振れで、12時台の帯内散発減衰 (run463-465 10/180) → run466 (0/60) からの帯移行時帯初 1 窓 heavy (run467A 8/20) への再上振れが「帯移行時帯初に heavy 再上振れ → 帯内で散発減衰」パターンを繰り返し、K-Z3 traffic 依存説の方向支持を継続 (日中帯高水準 12-13時台帯初 ~13.3% vs 朝帯境低位帯 6-7時台 ~1.7-2.2% の帯初集中入れ替わり、深夜帯 ~26-31% 平坦パターンとの対比不変)。heavy>=6/20 は帯初 run467A 8/20 で再現するも帯内持続は未確認 (run462A 帯初 8/20 同型 — 帯水準としての heavy 持続性は 13時台 n 追加で確認)。host load1 106 高騰の p50 上振れ込み borderline note 付きだが cold 8 件 1.19–1.91s は閾値決定的。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任 (transact 401 write path 調査), KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす決定的支持/反証に未達 — K-Z3 open 継続・帯初 n=1 セットで帯水準確定・機構判断未達, K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run 計測)。host load1 27.01 (13:40 uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本更新のみで影響なし。secret は一切記録せず。NEXT: K-Z3 13時台 n-add run468 (13時台帯初 run467 8/60 ~13.3% 帯初 heavy — 帯水準確定と heavy 帯内持続性の確認に 13時台 n 積み増し継続, 次枠 run468 を falsify/bench が実施)。\n"

anchor = "## Iteration log\n- 2026-09-08: bench 第193回。"
assert content.count(anchor) == 1, "anchor count: %d" % content.count(anchor)
new_header = "## Iteration log\n" + entry + "- 2026-09-08: bench 第193回。"
new_content = content.replace(anchor, new_header, 1)

assert new_content.count("## Iteration log") == 1, "header count != 1"
idx_h = new_content.index("## Iteration log")
idx_rank = new_content.index("rank 第209回")
assert idx_rank > idx_h, "rank entry not after header"
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("inserted OK; new length", len(new_content))