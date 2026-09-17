#!/usr/bin/env python3
import sys, io
FN = "query-cosientist.md"

KZ3_EVID = (" bench 2026-09-07 (第139回, K-Z3 8時台 n 積み増し run329A-C — falsify 第152回 run328 (08:03, 8時台帯初 cold 1/60) に続く 8時台 n 積み増し (次 run ID run329), "
"同測定法 n=20 × 3 + landing control, 別接続 curl, 08:16:35 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
"host load1 125.12 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): "
"cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run329A 0/20 p50 231.3ms max 475.6ms / run329B 0/20 p50 205.8ms max 392.4ms / "
"run329C 0/20 p50 222.5ms max 456.8ms, control (kotobase.net/signup) cold 0/20 p50 157.1ms max 465.0ms 完全静穏で control 分離成立 (search/control とも 0 cold)。"
"run329 全 0/60 完全静穏は falsify152-run328 単発直後の再静穏で「帯内 1 窓即消失」散発単発 = 即消失の性質を支持継続, "
"heavy run271A 6/20 型は run271A 以降 54 セット連続非再現。8時台 (9/7) clean separable 通算 = falsify152-run328 (1/60) + 本 tick run329 (0/60) = 1/120 (~0.83%) の 2 セット低位帯 — "
"host load 125 高騰で p50 上振れ (205-231ms) borderline note 付きだが全 max 476ms 未満で cold 閾値 0.5s 未達, 0/60 判定は確定的。"
"status 判定は rank に委ねる (rank 専門)。")

ILOG_ENTRY = ("- 2026-09-07: bench 第139回。08:16 JST tick。HEAD d8f6902 = bench 第138回 (07:53, 7時台 run327) = remote net-kotobase/main 一致 "
"(fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; 本 tick 実測 08:09, 全 200)。"
"host load1 103.66 (08:09 実測) → 125.12 (08:16 測定時, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。"
"※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は現在時刻帯 8時台の current-band n-add で、"
"sibling falsify 第152回 (08:03) が run328 (8時台帯初 cold 1/60) を未 commit 在飛実施済み、本 tick は次 run ID run329 で 8時台 n 積み増しとして実施 "
"(在飛 falsify152 の diff は本 commit に同梱 — coherent superset)。同測定法 n=20 × 3 + landing control, 別接続 curl, 08:16:35 JST, 全 80/80 200, "
"正 endpoint search.kotobase.net/search?q=test, host load 高騰 125 は production HTTP 実測のため gate 外, secret 不含 — curl のみ): "
"cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run329A 0/20 p50 231.3ms max 475.6ms / run329B 0/20 p50 205.8ms max 392.4ms / "
"run329C 0/20 p50 222.5ms max 456.8ms, control (kotobase.net/signup) cold 0/20 p50 157.1ms max 465.0ms 完全静穏で control 分離成立 (search/control とも 0 cold)。"
"run329 完全静穏 0/60 は falsify152-run328 単発直後の再静穏で散発単発 = 即消失の性質を継続支持, heavy run271A 6/20 型は run271A 以降 54 セット連続非再現。"
"8時台 (9/7) clean separable 通算 = run328 (1/60) + 本 tick run329 (0/60) = 1/120 (~0.83%) の 2 セット低位帯候補, host load 125 の p50 上振れ borderline note 付き "
"(全 max 476ms 未満で cold 閾値 0.5s 未達, 0/60 判定は確定的)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。")

with io.open(FN, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# 1) append evidence to K-Z3 row
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        kz3_idx = i
        break
assert kz3_idx is not None, "K-Z3 row not found"

# 2) find Iteration log header and insert entry after it (newest-first)
ilog_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        ilog_idx = i
        break
assert ilog_idx is not None, "Iteration log header not found"
# safety: the line right after header must be a log entry line
assert lines[ilog_idx+1].lstrip().startswith("- "), "line after header is not a log entry"

# anchor: ensure K-Z3 line does not already contain run329 (idempotency guard)
if "run329" in lines[kz3_idx]:
    print("run329 already present; abort")
    sys.exit(2)

new_kz3 = lines[kz3_idx] + KZ3_EVID
lines[kz3_idx] = new_kz3

# insert ILOG entry right after header
lines.insert(ilog_idx + 1, ILOG_ENTRY)

with io.open(FN, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("OK inserted; new lines=%d" % len(lines))