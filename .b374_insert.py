#!/usr/bin/env python3
# bench 第164回: insert run374 evidence into K-Z3 row + prepend iteration log entry
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    lines = f.readlines()

evid = (
    " bench 2026-09-07 (第164回, K-Z3 16時台 n積み増し run374A–C — "
    "iter-log HEAD 連鎖 (第163回 16:37, NEXT「16時台 n積み増し続行, 次 run ID run373 使用」) の run373 枠は sibling が 16:51 に in-flight 先行 "
    "(.b373 データ存在確認) のため run373→run374 に読替 (run216/run256/run263 precedent, 独立計測として採用可否は rank 判定に委ねる), "
    "同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, "
    "正 endpoint search.kotobase.net/search?q=test, 16:56:29–16:56:51 JST, 全 80/80 200, "
    "host load1 24.58→31.56 (16:56 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
    "secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — "
    "run374A cold 3/20 (1.460/2.034/1.117s 散発) p50 51.5ms / run374B cold 0/20 p50 53.7ms max 95.6ms "
    "/ run374C cold 0/20 p50 48.6ms max 328.3ms, control (kotobase.net/signup) cold 0/20 p50 51.2ms max 119.3ms "
    "完全静穏で control 分離成立、cold 群は search 側に局在。"
    "run374A 散発 3/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消逝」型継続 "
    "(16:51 sibling run373 と同時帯独立測定, 16時台 6 セット目。"
    "16時台 (9/7) 通算は rank の run372 両記録 (falsify 6/60 + bench163 1/60) 取込判定を待つ。"
    "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"
)

iterlog = (
    "\n- 2026-09-07: bench 第164回。16:56 JST tick。HEAD 5a817df = bench 第163回 (16:37) "
    "(16:37 以降に sibling falsify 第170回 run372 6/60, run373 16:51 in-flight が uncommitted) = remote "
    "net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, "
    "fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。"
    "live smoke 200 (/, /signup; pre-run ・本 tick 実測)。host load1 24.58→31.56 (16:56 uptime 実測, gate 7.5 大幅超過) "
    "のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
    "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — "
    "true progressive NEXT は iter-log HEAD (bench 第163回, 16:37)「委ねる; フォールバックは K-Z3 16時台 n 積み増し続行、次 run ID は run373 使用」"
    "の run373 枠を本 tick 実施するも run373 は sibling 16:51 in-flight (.b373 存在) のため run374 に読替。K-Z3 16時台 run374A–C 実測 "
    "(同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
    "正 endpoint search.kotobase.net/search?q=test, 16:56:29–16:56:51 JST, 全 80/80 200, secret 不含 — curl のみ): "
    "cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run374A cold 3/20 (1.460/2.034/1.117s 散発) p50 51.5ms "
    "/ run374B cold 0/20 p50 53.7ms max 95.6ms / run374C cold 0/20 p50 48.6ms max 328.3ms, "
    "control (kotobase.net/signup) cold 0/20 p50 51.2ms max 119.3ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
    "run374A 散発 3/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消逝」型継続 (16時台 6 セット目, "
    "16:51 sibling run373 と同時帯独立測定)。status 判定は rank に委ねる (rank 専門)。"
    "secret は一切記録せず。詳細は K-Z3 evidence 欄追記。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 16時台 n 積み増し続行、"
    "次 run ID は run375 使用)\n"
)

# Locate K-Z3 row: line starting with "| K-Z3 |"
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        kz3_idx = i
        break
if kz3_idx is None:
    print("ERR: no K-Z3 row found"); sys.exit(1)

row = lines[kz3_idx].rstrip("\n")
lines[kz3_idx] = row + evid + "\n"

# Prepend iteration log entry after "## Iteration log" header
ilog_idx = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == "## Iteration log":
        ilog_idx = i
        break
if ilog_idx is None:
    print("ERR: no '## Iteration log' header found"); sys.exit(1)
lines.insert(ilog_idx + 1, iterlog.lstrip("\n"))

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("OK insert done; lines=", len(lines))