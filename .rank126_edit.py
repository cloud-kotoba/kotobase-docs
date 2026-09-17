#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

# ---- 1) Insert rank 126 fold paragraph after the 124th fold, before the judgded-note ----
anchor_end = "ただし帯水準確定・機構判断には未達 (2時台帯 n=1、追加 n 継続、fallback 専門のまま)。status: K-Z3 open 継続 (決定的反証/支持に未達 — 1時台 13/540 ~2.4%・2時台帯初 1/60 は帯水準確定に至らず)。"
judg = "( K-Q2 / K-W1 / K-W2 / K-Z1 は判定済みのため rank 外 )"

fold = (
"第126回の 2時台(深夜帯) n 積み増し folds (rank 第125回 quiet tick 以降の新規 3 commit): "
"bench 第116回 run285A-C (9/7 02:10, 2時台 n 積み増し — rank 第124回 NEXT「2時台 n 積み増し継続 (次 run ID run285)」の run285 枠, cold 3/0/0 per 20 = 3/60 ~5.0% — run285A 散発配置 2/20 (1.6227s 5番目/1.1323s 7番目) + B 単発 1/20 (0.7172s 6番目), C 0/20, control 1/20 0.528s 境界値 → not-separated-leaning, search 側 3/60 は閾値決定的, heavy run271A 以降 13 セット非再現) "
"+ falsify 第130回 run286A-C (9/7 02:18, run285→run286 読替 — bench 第116回 run285 と ID 衝突のため (run216/256/263/278 前例), cold 1/0/0 per 20 = 1/60 ~1.7% — run286A 単発散発 1.6003s (2番目), B/C + control 0/20 即消失, control p50 0.136s max 0.364s 完全静穏分離成立, heavy run271A 以降 14 セット非再現) "
"+ bench 第117回 run287A-C (9/7 02:22, cold 1/0/0 per 20 = 1/60 ~1.7% — run287A 冒頭単発 1.6196s (1番目), B/C 0/20, control 1/20 0.763s → borderline not-separated-leaning, search 側 1/60 は閾値決定的, heavy run271A 以降 15 セット非再現) "
"を取込、2時台通算 = run284 (1/60) + run285 (3/60) + run286 (1/60) + run287 (1/60) = 6/240 (~2.5%) の 4 セット、deep-night 累計 run275..287 = 19/780 (~2.4%) の 13 セットで低位帯水準継続。全セット「帯内 1 窓即消失」散発単発/ペア型 (run284A 0.805s → run285A 2+B 1 → run286A 1 → run287A 1 の散発減弱振幅内, heavy は run271A 6/20 以降 15 セット連続非再現)。run285/run287 は control に cold/delay 1 件 (0.528s/0.763s 境界値) が出現し control 分離 borderline not-separated-leaning で機構判定として弱い (search 側 cold 濃度は閾値決定的)。2時台通算 ~2.5% は 24時台 (18/420 ~4.3%)・1時台 (13/540 ~2.4%) と同水準の低〜中位帯候補で、深夜帯 traffic 最低帯 (24/0/1/2時台) での cold 散発全セット連続再出現は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし run285/287 に control borderline + host load 高騰 (~37-49) p50 上振れ混入のため機構判定には追加 clean-tick n を要する。status: K-Z3 open 継続 (決定的反証/支持に未達 — 2時台 6/240 ~2.5% は 24/1時台と同水準で帯水準確定・機構判断に至らず)。"
)

if anchor_end not in txt:
    print("ANCHOR1 NOT FOUND", file=sys.stderr)
    sys.exit(1)
if judg not in txt:
    print("JUDG NOT FOUND", file=sys.stderr)
    sys.exit(1)

i = txt.index(anchor_end)
j = txt.index(judg, i)
# insert fold + newlines between anchor_end and judg
insert = "\n" + fold + "\n\n\n"
txt = txt[:i + len(anchor_end)] + insert + txt[i + len(anchor_end):]

# ---- 2) Update rank numbering line (第114回 -> 第126回) if present ----
old_rank_hdr = "rank (期待 gain × 確率, 2026-09-06 第114回):"
if old_rank_hdr in txt:
    txt = txt.replace(old_rank_hdr, "rank (期待 gain × 確率, 2026-09-06 第126回):", 1)

# ---- 3) Insert rank 126 Iteration-log entry at top of Iteration log ----
iter_hdr = "## Iteration log\n"
if iter_hdr not in txt:
    print("ITER HDR NOT FOUND", file=sys.stderr)
    sys.exit(1)

entry = (
"- 2026-09-07: rank 第126回。02:33 JST tick。HEAD 36e4e50 = bench 第117回 (run287A-C, 02:22-02:24, 2時台 n 積み増し, cold 1/60 ~1.7%) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。rank 第125回 (cf1c37d, 02:18, quiet tick — 0 new evidence と判定) 以降の新規確定 evidence は 3 commit、いずれも K-Z3: bench 第116回 run285A-C (6d1262e, 02:10, 2時台 n 積み増し, cold 3/60 ~5.0% — run285A 散発配置 2/20 + B 単発 1/20, control 1/20 0.528s 境界値 borderline not-separated-leaning, search 側 3/60 閾値決定的) + falsify 第130回 run286A-C (cf784de, 02:18, run285→run286 読替 — bench 第116回 run285 と ID 衝突のため (run216/256/263/278 前例), cold 1/60 ~1.7% — run286A 単発散発 1.6003s, B/C + control 0/20 即消失, control 完全静穏分離成立) + bench 第117回 run287A-C (36e4e50, 02:22, cold 1/60 ~1.7% — run287A 冒頭単発 1.6196s, B/C 0/20, control 1/20 0.763s borderline not-separated-leaning, search 側 1/60 閾値決定的)。取り込み判定: (a) K-Z3: run285 + run286 + run287 を取込、2時台通算 = run284 (1/60) + run285 (3/60) + run286 (1/60) + run287 (1/60) = 6/240 (~2.5%) の 4 セット、deep-night 累計 run275..287 = 19/780 (~2.4%) の 13 セットで低位帯水準継続。全セット「帯内 1 窓即消失」散発単発/ペア型で heavy クラスタ (run271A 6/20 型) は run271A 以降 15 セット連続非再現。run285/287 は control 1 件 (0.528s/0.763s 境界値) borderline not-separated-leaning で機構判定は弱いが search 側 cold 濃度は閾値決定的。2時台 ~2.5% は 24時台 (18/420 ~4.3%)・1時台 (13/540 ~2.4%) と同水準の低〜中位帯候補で、深夜帯 traffic 最低帯 (24/0/1/2時台) での cold 散発全セット連続再出現は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status: K-Z3 open 継続 (決定的反証/支持に未達 — 2時台 6/240 ~2.5% は帯水準確定・機構判断に至らず)。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・2時台 6/240 ~2.5% は 24/1時台と同水準で帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 2時台 ~2.5% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 50.47 (02:32 uptime 実測, gate 7.5 大幅超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。NEXT (Iteration log 末尾): K-Z3 2時台(深夜帯) n 積み増し継続 (次 run ID run288)。secret は一切記録せず。\n"
)
txt = txt.replace(iter_hdr, iter_hdr + entry, 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)

print("OK: fold inserted, rank header updated, iter-log entry added")