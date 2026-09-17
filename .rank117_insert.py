#!/usr/bin/env python3
# Insert rank 117 entry into Iteration log of query-cosientist.md
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

entry = """## Iteration log
- 2026-09-07: rank 第117回。00:03 JST tick。HEAD 9b986d7 = remote net-kotobase/main 一致 (fetch net-kotobase + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。rank 第116回 (b616d8e, 23:48) 以降の新規確定 evidence は 2 本、いずれも K-Z3: (1) bench 第108回 run267A-C (fe84c1e, 23:55, committed, 23時台 n 積み増し, cold 5/60 ~8.3% — run267A 冒頭集中 3 件 + 中盤/末尾散発 2 件 1.10-2.09s, B/C 0/20 即消失, control cold 0/20 完全静穏で分離成立, run264/265/266 の連続 1/60 散発減弱からの弱い再上振れで run260A 8/20 / run263A 5/20 型 heavy 寄り散発クラスタの再現方向, host load 38 高騰の p50 上振れ込み borderline だが cold 5 件 1.10-2.09s は閾値決定的), (2) falsify 第122回 run268A-C (9b986d7, 00:00, committed, 24時台(0時台)帯初計測, cold 2/60 ~3.3% — run268A 中盤隣接ペア 2/20 1.757s/1.353s, B/C 0/20 即消失, control cold 0/20 静穏で分離成立, run266A 単発 / run267A 5/20 の中間帯散発型)。取り込み判定: (a) K-Z3: run267 を取込 23時台通算 = 25/480 (~5.2%) + 5/60 = 30/540 (~5.6%) の 9 セット連続 cold>0 (帯初 heavy → 連続 1/60 散発減弱 → run267 弱い再上振れの合成、run260A 8/20 / run263A 5/20 型 heavy は本 tick まで本格再現なし、全セット「帯内 1 窓即消失」(B/C 0/20, control 分離成立) 型)。24時台(0時台)帯初計測 run268 (2/60 ~3.3%) は 23時台 (~5.6%) と同水準の低〜中位帯候補で、深夜帯 (traffic 最低帯) での cold 出現継続は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。但し 24時台は帯初 n=1 セットで帯水準確定・機構判断には未達 — 追加 n 継続 (fallback 専門のまま)。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・23時台 30/540 ~5.6% / 24時台帯初 2/60 ~3.3% は帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 23時台 ~5.6% / 24時台帯初 ~3.3% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 20.38/24.98/27.83 (00:02 uptime 実測, gate 7.5 超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。
  NEXT: K-Z3 24時台 n 積み増し継続 — 24時台(0時台)帯初計測 run268 (2/60 ~3.3%) は 23時台 (30/540 ~5.6%) と同水準の低〜中位帯候補が立ち、現時刻帯 0時台(24時台)の間は 24時台 n 積み増し、時間帯移行後は次の帯初/帯確定へ (深夜帯 ~26-31% 平坦パターンへの収束か 24時台限局かは追加 n 継続のみで判別)。host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run269 使用。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。
"""

marker = "## Iteration log\n- 2026-09-07: falsify 第122回。00:00 JST tick。"
if marker not in content:
    print("MARKER NOT FOUND", file=sys.stderr)
    sys.exit(1)
if "rank 第117回" in content:
    print("ALREADY INSERTED", file=sys.stderr)
    sys.exit(0)

new_content = content.replace(marker, entry, 1)
with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("INSERT_OK r117")