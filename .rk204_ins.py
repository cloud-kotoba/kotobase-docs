import io
p = 'query-cosientist.md'
txt = io.open(p, encoding='utf-8').read()
lines = txt.split('\n')
hdr = None
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        hdr = i
        break
assert hdr is not None, 'header not found'
assert lines[hdr+1].startswith('- 2026-09-08: falsify 第207回'), 'anchor mismatch: %r' % lines[hdr+1][:60]

new_entry = ("- 2026-09-08: rank 第204回。11:50 JST tick。HEAD c7af527 = falsify 第207回 (11:38, K-Z3 11時台 n-add run461 cold 2/60 ~3.3% — run461A 散発単発 2/20 (1.1789s / 2.0231s), B/C 0/40, control 0/20 完全静穏分離成立; 前 HEAD 94e60e0 = bench 第204回 run460 cold 4/60 ~6.7%) = remote bench_fetch/main・net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; ※本 tick 開始時 worktree に sibling bench 第204回 (run460) の未 commit iter-log 行が在り git diff HEAD 非 empty — 挿入・上書きせず ~40s 待機+再 fetch で bench 第204回 commit (94e60e0) 着弾、続いて falsify 第207回 commit (c7af527) も着弾し HEAD 前進・diff empty 化を確認の上 c7af527 上へ単一 rank 行のみ挿入, header=1 事前確認済; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 5.70 (11:50 uptime 実測) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第203回→bench 第204回 run460→falsify 第207回 run461)。rank 第203回 (6a924be, 11:27) 以降の新規確定 evidence は 2 commit、すべて K-Z3 11時台 (9/8): (a) bench 第204回 commit (94e60e0, 11:31) の run460: cold(>=0.5s) 4/60 ~6.7% — run460A 頭近接 3/20 (1.7485s pos2 / 1.1579s pos6 / 1.1871s pos7) + run460C 単発 1/20 (1.4184s pos14), B 0/20, control (signup) 0/20 完全静穏で分離成立, cold は search 側局在, run459A クラスタ 4/20 の弱い再現。(b) falsify 第207回 commit (c7af527, 11:38) の run461 (11時台 5 セット目): cold 2/60 ~3.3% — run461A 分散/単発 2/20 (1.1789s / 2.0231s), B/C 0/40, control 0/20 完全静穏分離成立, heavy>=6/20 非再現継続。取り込み判定: (a) K-Z3: run460 + run461 を 11時台通算に積み上げ、11時台 (9/8) 通算 = run457 (2/60) + run458 (0/60) + run459 (5/60) + run460 (4/60) + run461 (2/60) = 13/300 (~4.3%) の 5 セット低〜中位帯候補継続 — 9時台 (11/300 ~3.7%)・10時台 (17/420 ~4.0%) と同水準の日中帯低〜中位帯継続, セット間変動大 (run459 5/60 vs run458 0/60, run460 4/60 vs run461 2/60), 単発+近接クラスタ型が混在, control 全セット完全静穏分離成立・heavy>=6/20 非再現継続, K-Z3 traffic 依存説への方向支持継続・強反証材料なし。帯水準確定・機構判断には rank 追加 n を要する。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・帯水準確定未達 (11時台 n=5 セット), 他は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — K-Z3 11時台 13/300 ~4.3% は順位不変, 帯水準確定は後続 n 次第)。secret は一切記録せず。")

out = lines[:hdr+1] + [new_entry] + lines[hdr+1:]
io.open(p, 'w', encoding='utf-8').write('\n'.join(out))
print('inserted at', hdr+2)