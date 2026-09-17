#!/usr/bin/env python3
# rank 119: insert iteration-log entry at top of Iteration log section
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the "## Iteration log" header
hdr = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == "## Iteration log":
        hdr = i
        break
assert hdr is not None, "Iteration log header not found"

entry = """- 2026-09-07: rank 第119回。00:33 JST tick。HEAD 3a19846 = remote net-kotobase/main 一致
  (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取り込み)。
  rank 第118回 (82274f7, 00:25) 以降の新規確定 evidence は 1 commit — falsify 第124回
  run271A-C (3a19846, 00:31, 24時台(0時台) n 積み増し, cold 6/1/0 per 20 = 7/60 ~11.7% —
  run271A heavy 散発クラスタ 6/20 0.9385/1.0773/1.1442/1.1642/1.5370/1.8709s (冒頭+中盤散発配置,
  warm 群と交互), run271B 単発 1.2019s 1/20, run271C 0/20, B/C + control 0/20 即消失・完全静穏分離
  成立, control (kotobase.net/signup) cold 0/20 p50 0.042s max 0.332s — run269A 3/20 → run270A 1/20
  の散発減弱からの再上昇で run260A 8/20 / run263A 5/20 / run267A 5/20 型 heavy の弱い再現, 24時台総
  = run268 2/60 + run269 3/60 + run270 1/60 + 本 tick 7/60 = 13/240 (~5.4%) の 4 セット連続 cold>0)。
  取り込み判定: (a) K-Z3: run271 を取込 24時台通算 13/240 (~5.4%) の 4 セット連続 cold>0 —
  run271A heavy 6/20 再上振れは B/C + control 0/20 で即消失し「帯内 1 窓即消失」型の中で散発減弱
  (1/60) → heavy 寄り再上昇 (6/20) の振幅が 24時台内で確認された。深夜帯 24/0時台 (traffic 最低帯)
  での cold 連続出現 + heavy 再上振れは K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦
  パターンと整合方向)。ただし全セット「帯内 1 窓即消失」(B/C 0/20, control 分離成立) 型で帯水準確定・
  機構判断には未達 (追加 n 継続, fallback 専門のまま)。(b) K-Q1: 変動なし — transact 401 の静的切れ手
  (a)/(i)/(ii)/(iii) は全て棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit
  delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/
  K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は
  cosientist 実装待ち, K-Z3 は観測継続・24時台 13/240 ~5.4% は帯水準確定・機構判断に至らず, K-Z2/
  K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位
  変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 24時台 ~5.4% は順位を変えない)。live smoke 200 (/,
  /signup; pre-run 計測)。host load1 20.33/26.27/29.16 (00:32 uptime 実測, gate 7.5 超過) — rank 担当は
  測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。
  NEXT: K-Z3 24時台(0時台) n 積み増し継続 — 24時台は 4 セット連続 cold>0 で通算 13/240 (~5.4%) の
  低〜中位帯候補 (run269A 3/20 → run270A 1/20 散発減弱 → run271A 6/20 heavy 寄り再上昇の振幅確認,
  heavy は帯内 1 窓型で非定着) が立ち、現時刻 0時台(24時台) の間は 24時台 n 積み増し、時間帯移行後は
  次の帯初/帯確定へ (深夜帯 ~26-31% 平坦パターンへの収束か 24時台限局かは追加 n 継続のみで判別)。
  host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run272 使用。
  K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit
  delegation 動的照合)。
"""

# Insert after the header (keep header + its blank line handling simple)
lines.insert(hdr + 1, entry)

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

sys.stdout.write("inserted after line %d; new total lines = %d\n" % (hdr + 1, len(lines)))