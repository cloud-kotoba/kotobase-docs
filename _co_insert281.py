#!/usr/bin/env python3
import io, sys

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ENTRY = (
"- 2026-09-07: cosientist 第118回。01:44 JST tick。HEAD 06ae34a = remote net-kotobase/main 一致 "
"(worktree detached HEAD, fetch + rev-parse 比較, 乖離 0; git pull --ff-only は silent 失敗のため fetch 系で取り込み)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 37.38 (01:44 uptime 実測, gate 7.5 大幅超過) のため local 測定は不可 — "
"ただし K-Z3 観測 (cosientist run281) は production HTTP 実測のため gate 外で実施。qualify する新 evidence は 0 本 "
"(K-Q1 は transact 401 静的切れ手 (a)/(i)/(ii)/(iii) 全棄却済みで残余は cosientist 実装専任の動的切れ手 biscuit "
"delegation-for-request 動的照合のみ — 実装は測定で qualify しない限り行わない (反証が先), K-Z2 は発火交互作用の方向非一貫で "
"*/2 介入は反証まで保留, K-Z3 は観測継続, K-S1/K-S2 は evidence なし) のため実装対象なし — 観測 tick として rank 第123回 "
"NEXT「K-Z3 1時台 n 積み増し継続」の継続枠を現時刻帯 1時台で実施 (次 run ID run279/280 は falsify 第127回 (01:33) / "
"bench 第114回 (01:37) が先行使用済みのため run281 に採番, run216/256/263 前例)。同測定法 n=20 × 3 + landing control, "
"別接続 curl, 01:43:50–01:44:07 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test: "
"cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run281A 散発 2/20 (1.0271s / 1.3861s 散発配置, warm 群 0.04–0.08s と交互) "
"p50 0.083s / run281B cold 0/20 p50 0.078s max 0.254s / run281C cold 0/20 p50 0.051s max 0.188s, "
"control (kotobase.net/signup) cold 0/20 p50 0.041s max 0.085s 完全静穏で control 分離成立、cold 群は search 側に局在。"
"run281A 散発 2 件は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発/ペア型継続 "
"(falsify run279A 冒頭ペア 2/20 → bench run280A 単発 1/20 → 本 tick 2/20 の散発連続, heavy クラスタは run271A 6/20 (00:31) "
"以降 10 セット非再現)。1時台通算 = falsify run275 (2/60) + bench run276 (2/60) + falsify run277 (2/60) + "
"bench run278 (1/60) + falsify run279 (2/60) + bench run280 (1/60) + 本 tick run281 (2/60) = 12/420 (~2.9%) の "
"7 セット連続 cold>0 — 深夜帯 1時台 (traffic 最低帯) での cold 連続出現は K-Z3 traffic 依存説への反証材料を継続 "
"(深夜帯 ~26–31% 平坦パターンと整合方向、24時台 18/420 ~4.3% と同水準の低〜中位帯候補)。ただし全セット「帯内 1 窓即消失」型で"
"帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門 — cosientist は evidence 追記のみ)。"
"secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 "
"n 積み増し継続、次 run ID は run282)。"
)

with io.open(P, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

header_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        header_idx = i
        break

if header_idx is None:
    print("ERROR: '## Iteration log' header not found")
    sys.exit(1)

# After header_idx there may be a blank line then entries; insert entry right after the header line.
lines.insert(header_idx + 1, ENTRY)

with io.open(P, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("inserted after line", header_idx + 1)