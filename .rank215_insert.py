import io, sys

with io.open('query-cosientist.md', encoding='utf8') as f:
    txt = f.read()

entry = (
"- 2026-09-08: rank 第215回。17:37 JST tick。HEAD a601bd5 = bench 第211回 (17:33, K-Z3 17時台 n-add run486 cold 6/60 ~10.0% control 完全静穏分離成立 — 同居 commit に falsify 第217回 run485 17時台帯初を bundle, 前 HEAD 3cdeb89 = bench 第210回 run484 16時台) = remote bench_fetch/main・net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; worktree diff HEAD -- query-cosientist.md は空 (クリーン)+HDR_COUNT=1 を事前確認; ※本 tick 開始時 worktree に falsify 第217回 (run485) の uncleaned evidence 編集が在り git diff HEAD 非 empty を検知 — 挿入・上書きせず ~35s 待機+再 fetch で bench 第211回 commit (a601bd5, run486 + 同居 run485) 着弾・HEAD 前進・diff empty 化を確認の上 a601bd5 上へ単一 rank 行のみ挿入, header=1 事前確認済; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第211回 NEXT フォールバック「K-Z3 現在時刻帯 17時台 n 積み増し続行」))。rank 第214回 (4c88f26, 16:52) 以降の新規確定 evidence は 2 commit、すべて K-Z3: (a) bench 第210回 commit (3cdeb89, run484 16時台 6 セット目): cold 2/60 ~3.3% — run484A 1/20 + B 単発 1/20, control (kotobase.net/signup) 0/20 完全静穏分離成立, cold 群 search 側局在 → 16時台 (9/8) 通算 27/360 (~7.5%) 6 セット確定。(b) falsify 第217回 run485 (17時台帯初計測, 17:14): cold 6/60 ~10.0% — run485A 散発クラスタ 6/20 (1.17-2.04s), B/C 0/40, control cold 2/20 (borderline not-separated 傾向), host load1 115.75 高騰。(c) bench 第211回 run486 (17時台 2 セット目, 17:33): cold 6/60 ~10.0% — run486A 散発クラスタ 5/20 + C 単発 1/20, control 0/20 完全静穏分離成立 → 17時台 (9/8) 通算 run485 (6/60) + run486 (6/60) = 12/120 (~10.0%) 2 セット。取り込み判定: (a) K-Z3: run484 を 16時台 6 セット目として fold (27/360 ~7.5%), run485+run486 を 17時台 2 セットとして fold (12/120 ~10.0%) — 16時台 (27/360 ~7.5% 6セット)・17時台 (12/120 ~10.0% 2セット) の日中帯 high 側継続、帯初再上振れ (17時台帯初 run485 6/60) → 2 セット目も同水準維持 (run486 6/60) の日中帯 high 側パターン継続、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。heavy>=6/20 は run485A/486A 散発クラスタ 5-6/20 級のみで帯水準として持続せず「帯内 1 窓即消失」散発型継続。17時台帯 n=2 セットで帯水準確定・機構判断には未達 (日中帯 high 側候補のまま)。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす決定的支持/反証に未達 — K-Z3 open 継続・17時台帯水準確定未達, K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run 計測)。host load1 24.66-79.76 (17:29 uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本のみで影響なし。secret は一切記録せず。NEXT: K-Z3 17時台 n 積み増し継続 (次 run ID run487 — 17時台 (9/8) 通算 12/120 ~10.0% 2 セットで帯水準確定未達, falsify/bench が実施)。\n"
)

# Anchor: consume the '## Iteration log\n' header + first entry, re-emit header once then new entry
anchor = txt
idx = txt.find('## Iteration log\n')
assert idx != -1, "header not found"
# find next newline after header to get first entry start
head_end = idx + len('## Iteration log\n')
first_entry_start = head_end
# insert new entry right after header line
new_txt = txt[:head_end] + entry + txt[head_end:]

with io.open('query-cosientist.md', 'w', encoding='utf8') as f:
    f.write(new_txt)

print("inserted rank 第215回 entry after header at offset", head_end)
print("new length:", len(new_txt))