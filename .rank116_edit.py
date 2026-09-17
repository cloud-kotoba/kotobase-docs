#!/usr/bin/env python3
import io, sys

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

anchor = "## Iteration log\n- 2026-09-06: falsify 第121回。23:47 JST tick。"
if anchor not in content:
    print("ANCHOR NOT FOUND; abort"); sys.exit(1)

entry = (
"- 2026-09-06: rank 第116回。23:48 JST tick。HEAD cbbeac1 = remote net-kotobase/main 一致 "
"(fetch net-kotobase rc 0 + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。"
"rank 第115回 (65e7fc9, 23:39) 以降の新規確定 evidence は 3 本、いずれも K-Z3 23時台 n 積み増し: "
"(1) bench 第107回 run264A-C (cbbeac1, 23:40, committed, cold 1/60 ~1.7% — run264A 単発 1.324s 散発, B/C 0/20 即消失, control cold 0/20 静穏で分離成立, run260A/263A heavy の非再現・散発減弱方向), "
"(2) cosientist 第116回 run265A-C (286b9b5, 23:44, committed, cold 1/60 ~1.7% — run265A 単発, control 静穏分離成立, 単発型継続), "
"(3) falsify 第121回 run266A-C (23:47, worktree in-flight 未 commit, cold 1/60 ~1.7% — run266A 単発 1.2092s 19番目, B/C 0/20 即消失, control cold 0/20 完全静穏で分離成立, run264/265 は既使用のため run266 に読替の独立 計測)。"
"取り込み判定: (a) K-Z3: run264/265/266 を取込 23時台通算 = run260 (8/60) + run259 (4/60) + run261 (3/60) + run262 (2/60) + run263 (5/60) + run264 (1/60) + run265 (1/60) + run266 (1/60) = 25/480 (~5.2%) の 8 セット連続 cold>0 "
"— 帯初 3 セット (run260 8 + run259 4 + run261 3 = ~8.3-10% 高位) から連続 3 セット 1/60 へ散発減弱が継続し、run260A (8/20) / run263A (5/20) 型 heavy クラスタの再現なし、帯内全セット「帯内 1 窓即消失」(B/C 0/20, control 分離成立) 型で 23時台は ~5.2% の低位帯残界へ収束傾向。"
"深夜帯 23時台 (traffic 最低帯) で cold 連続出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向) だが、8 セットとも散発単発で帯水準確定・機構判断には未達。追加 n の限界情報利得は低下継続 (fallback 専門のまま)。"
"(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。"
"(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・23時台 25/480 ~5.2% は帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。"
"新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 23時台 ~5.2% は順位を変えない)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 13.69 (23:47 uptime 実測, gate 7.5 超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。\n"
"  NEXT: K-Z3 23時台 n 積み増し継続 — 23時台は 8 セット通算 25/480 (~5.2%) の低位帯残界へ収束傾向 (帯初 heavy から連続 1/60 散発減弱, heavy 非再現) が立ち、現時刻 23時台の間は 23時台 n 積み増し、24時台移行後は 24時台帯初計測へ (深夜帯 ~26-31% 平坦パターンへの収束か 23時台限局上振れかの判別は追加 n 継続のみ)。host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run267 使用。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。\n"
)

content = content.replace(anchor, "## Iteration log\n" + entry + "- 2026-09-06: falsify 第121回。23:47 JST tick。", 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("INSERTED rank 第116回 entry")