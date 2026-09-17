#!/usr/bin/env python3
import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    content = f.read()
lines = content.split("\n")

# find '## Iteration log' header (first occurrence)
hdr = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        hdr = i
        break
assert hdr is not None, "Iteration log header not found"

entry = ("- 2026-09-07: bench 第179回。21:32 JST tick。HEAD e343910 = bench 第178回 (21:11, K-Z3 21hr "
    "band-first run397 cold 3/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; "
    "worktree detached HEAD のため fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力は "
    "ファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 22.80 (21:32 uptime 実測, "
    "gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
    "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true "
    "progressive NEXT は iter-log HEAD (bench 第178回)「委ねる (falsify/bench フォールバックは K-Z3 現在時刻帯 "
    "21時台 n 積み増し続行、次 run ID は run398 使用)」の run398 枠を本 tick 実施 (21時台帯first run397 済みの "
    "積み増し, run398 は commit 未使用で衝突なし確認, .b398 既存なし)。K-Z3 21時台 run398A–C 実測 "
    "(同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
    "search.kotobase.net/search?q=test, 21:31:49–21:32:04 JST, 全 80/80 200, secret 不含 — curl + python "
    "stats のみ): cold(>=0.5s) 6/0/0 per 20 = 6/60 (~10.0%) — run398A cold 6/20 散発クラスタ "
    "(1.8146s pos1 / 1.1017s pos2 / 1.0152s pos7 / 1.1853s pos12 / 1.3640s pos18 / 1.0633s pos19) "
    "p50 59.9ms / run398B cold 0/20 p50 46.7ms max 152.8ms / run398C cold 0/20 p50 56.1ms max 179.8ms, "
    "control (kotobase.net/signup) cold 0/20 p50 53.4ms max 409.8ms 完全静穏で control 分離成立、cold 群は "
    "search 側に局在。run398A 散発クラスタ 6/20 (1.0–1.8s deep) は B/C 0/40 即消失で「帯内 1 窓即消失」"
    "散発クラスタ型継続 — 21時台 (9/7) 通算 = falsify-run397 2/60 + bench-178-run397 3/60 + 本 tick 6/60 = "
    "11/180 (~6.1%) の 3 セット中位〜低位帯候補, 20時台 (20/360 ~5.6%)・9/6 21時台 (~3.0%) と同水準の帯横断継続"
    " (日中帯 traffic 依存説の夜帯低位方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は "
    "rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 21時台 n 積み増し続行、次 run ID は run399 "
    "使用 — ※sibling falsify/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)。")

lines.insert(hdr + 1, entry)
with io.open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

with io.open(path, encoding="utf-8") as f:
    v = f.read().split("\n")
print("ENTRY inserted at line", hdr+2, "| check:", "bench 第179回" in v[hdr+2])
print("header line still:", v[hdr])