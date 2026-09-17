#!/usr/bin/env python3
import sys

PATH = "query-cosientist.md"
HDR = "## Iteration log"

entry = """- 2026-09-07: cosientist 第125回。17:03 JST tick。HEAD 207bc7e = falsify 第171回 (17:01, K-Z3 16時台 run373 cold 7/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 21.88→22.15 (17:03 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (bench 第164回, 16:56)「K-Z3 現在時刻帯 16時台 n 積み増し続行、次 run ID は run375 使用」の run375 枠だが、本 tick 実行時刻 17:03 は 16時台 (16:00–16:59) 終了後の 17時台開始帯に当たるため run375 を 17時台帯初計測として実施 (.b375 データ 既存なし=衝突なし確認, 17時台 1 セット目)。K-Z3 17時台 run375A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 17:03:27–17:03:42 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 3/1/0 per 20 = 4/60 (~6.7%) — run375A cold 3/20 散発 (1.0647s pos4 / 1.2996s pos6 / 2.0563s pos13 散発配置) p50 82ms / run375B cold 1/20 (1.0990s pos2 単発) p50 60ms / run375C cold 0/20 p50 63ms max 189ms, control (kotobase.net/signup) cold 0/20 p50 55ms max 105ms 完全静穏で control 分離成立、cold 群は search 側に局在。run375A 散発 3/20 + B 単発は C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発型継続 (17時台帯初計測 cold 4/60 ~6.7%, heavy>=6/20 は再達せず run368A/373A heavy 型は非再現継続)。17時台 (9/7) 帯初サンプル cold 4/60 (~6.7%) — 16時台 (9/7) 通算 33/360 ~9.2% の高位帯候補とは異なる独立帯初で、日中帯高位パターン方向の帯横断追加観測として記録 (帯水準確定は rank 追加 n を要する)。qualify する新 evidence は 0 本 (K-Q1 は残余が cosientist 実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ — 実装は測定で qualify しない限り行わない (反証が先), K-Z2 は発火交互作用方向非一貫で介入保留, K-Z3 は観測継続, K-S1/K-S2 は evidence なし) のため cosientist 実装対象なし — 観測 tick。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 17時台 n 積み増し続行、次 run ID は run376 使用)
"""

with open(PATH, "r") as f:
    lines = f.readlines()

# find the header line
idx = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == HDR:
        idx = i
        break
if idx is None:
    print("HEADER NOT FOUND")
    sys.exit(1)

# insert entry right after header (before existing first entry)
insert_at = idx + 1
lines[insert_at:insert_at] = [entry]

# guard: do not duplicate if entry already present
joined = "".join(lines)
if "cosientist 第125回" in open(PATH).read():
    print("ALREADY PRESENT, SKIP")
    sys.exit(0)

with open(PATH, "w") as f:
    f.writelines(lines)
print("INSERTED at line", insert_at + 1)