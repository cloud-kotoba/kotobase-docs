#!/usr/bin/env python3
# rank127_edit.py (v2) — corrected to fold BOTH run290 measurements.
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    s = f.read()

# --- Edit 1: rank body header ---
h_old = "rank (期待 gain × 確率, 2026-09-06 第126回):"
h_new = "rank (期待 gain × 確率, 2026-09-07 第127回):"
if h_old in s:
    s = s.replace(h_old, h_new, 1)
    print("EDIT1 header: OK")
else:
    print("EDIT1 header: NOT FOUND", file=sys.stderr)

# --- Edit 2: append 第127回 fold after 第126回 fold paragraph ---
anchor = "status: K-Z3 open 継続 (決定的反証/支持に未達 — 2時台 6/240 ~2.5% は 24/1時台と同水準で帯水準確定・機構判断に至らず)。"
fold = """
第127回の 2時台(深夜帯) n 積み増し folds (rank 第126回 以降の新規 4 commit — falsify 第131回 run288, bench 第118回 run289, falsify 第132回 run290, bench 第119回 run290):
- falsify 第131回 run288A-C (9/7 02:31-02:32, 2時台 n 積み増し, cold 1/60 ~1.7% — run288B 単発散発 1.5296s (6番目), A/C + control 0/20 即消失, control 完全静穏分離成立, heavy run271A 以降 16 セット非再現)
- bench 第118回 run289A-C (9/7 02:40, cold 0/60 完全静穏 — run289A/B/C 全 0/20 + control 0/20, p50 41-43ms, 2時台 cold>0 5 セット連続 (run284-288) を打破, 完全静穏 0/60 は run283 型 2 例目, heavy 以降 17 セット非再現)
- falsify 第132回 run290A-C (9/7 02:46, cold 1/60 ~1.7% — run290A 単発散発 1.3134s (15番目), B/C + control 0/20 即消失, control 完全静穏分離成立, run289 完全静穏直後の 1 件再出現 = 散発単発即消失の性質と整合, heavy 17 セット非再現)
- bench 第119回 run290A-C (9/7 02:53-02:54, run290 ID 衝突の独立計測 — falsify 第132回 run290 が先行使用のため (run105/193/216/224 前例で両方採用), cold 1/60 ~1.7% — run290A 単発 1.442s (2番目), B/C + control 0/20 即消失, control 完全静穏分離成立, heavy 17 セット非再現)
を取込、2時台通算 = run284 (1/60) + run285 (3/60) + run286 (1/60) + run287 (1/60) + run288 (1/60) + run289 (0/60) + falsify-run290 (1/60) + bench-run290 (1/60) = 9/480 (~1.9%) の 8 セット、deep-night 累計 run275..290 (両 run290 換入) = 22/1020 (~2.2%) の 17 セットで低位帯水準継続。全セット「帯内 1 窓即消失」散発単発/ペア型 (run288B 単発 → run289 完全静穏 → falsify-run290A 単発 → bench-run290A 単発の振幅内, heavy は run271A 6/20 以降 18 セット連続非再現)。run289/両 run290 は control 完全静穏で機構判定として clean (run288 も control 静穏分離成立)。2時台通算 ~1.9% は 24時台 (18/420 ~4.3%)・1時台 (13/540 ~2.4%) と同水準の低〜中位帯候補で、深夜帯 traffic 最低帯 (24/0/1/2時台) での cold 散発継続 (完全静穏 2 窓を挟みながら) は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし帯水準確定・機構判断には未達 (追加 n 継続、fallback 専門のまま)。status: K-Z3 open 継続 (決定的反証/支持に未達 — 2時台 9/480 ~1.9% は 24/1時台と同水準で帯水準確定・機構判断に至らず)。"""
if anchor in s:
    s = s.replace(anchor, anchor + fold, 1)
    print("EDIT2 fold: OK")
else:
    print("EDIT2 fold: ANCHOR NOT FOUND", file=sys.stderr)

# --- Edit 3: Iteration log entry (insert new newest-first, after "## Iteration log" header) ---
log_header = "## Iteration log\n"
entry = """- 2026-09-07: rank 第127回。02:57 JST tick。HEAD 2369429 = bench 第119回 (run290 ID 衝突の独立計測, 02:53-02:54, 2時台 n 積み増し, cold 1/60 ~1.7%) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; 本 tick は terminal foreground 出力が空で戻る既知 runtime 障害のため出力をファイル書き出し経由で確認)。rank 第126回 (6620922, 02:33, run287 まで fold) 以降の新規確定 evidence は 4 commit、いずれも K-Z3 2時台: falsify 第131回 run288A-C (306d186, 02:31-02:32, cold 1/60 ~1.7%) + bench 第118回 run289A-C (952d7f0, 02:40, cold 0/60 完全静穏 — 2時台 cold>0 5 セット連続 (run284-288) 打破, run283 型 2 例目) + falsify 第132回 run290A-C (8b87eeb, 02:46, cold 1/60 ~1.7%) + bench 第119回 run290A-C (2369429, 02:53-02:54, cold 1/60 ~1.7%, run290 ID 衝突の独立計測 — run105/193/216/224 前例で両方採用)。取り込み判定: (a) K-Z3: run288+run289+両 run290 を取込、2時台通算 = run284 (1/60) + run285 (3/60) + run286 (1/60) + run287 (1/60) + run288 (1/60) + run289 (0/60) + falsify-run290 (1/60) + bench-run290 (1/60) = 9/480 (~1.9%) の 8 セット、deep-night 累計 run275..290 (両 run290 換入) = 22/1020 (~2.2%) の 17 セットで低位帯水準継続。全セット「帯内 1 窓即消失」散発単発/ペア型で heavy クラスタ (run271A 6/20 型) は run271A 以降 18 セット連続非再現。run289 完全静穏 (run283 型 2 例目) + 両 run290A の直後単発再出現で散発単発=即消失の性質がさらに支持される。2時台 ~1.9% は 24時台 (18/420 ~4.3%)・1時台 (13/540 ~2.4%) と同水準の低〜中位帯候補で、深夜帯 traffic 最低帯での cold 散発継続は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status: K-Z3 open 継続 (決定的反証/支持に未達 — 2時台 9/480 ~1.9% は帯水準確定・機構判断に至らず)。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・2時台 9/480 ~1.9% は帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 2時台 ~1.9% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 28.41 (02:47 uptime 実測, gate 7.5 超過) のため rank は測定を行わず状態正本の更新のみ。secret は一切記録せず。
  NEXT: K-Z3 現在時刻帯 n 積み増し継続 (現時刻 02:57 — 次 run ID は run291; cron 実行時刻が帯移行した場合は現時刻帯で実施, falsify 第129回 precedent)。
"""
if log_header in s:
    s = s.replace(log_header, log_header + entry, 1)
    print("EDIT3 iterlog: OK")
else:
    print("EDIT3 iterlog: HEADER NOT FOUND", file=sys.stderr)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(s)
print("written, len chars =", len(s))