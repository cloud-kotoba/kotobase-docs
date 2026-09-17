#!/usr/bin/env python3
# bench run506: append evidence to K-Z3 row (L279) + insert iter-log entry after header.
# ASCII/japanese in source; uses string anchors (not line numbers) for robustness.
import io, sys

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
def readp():
    return io.open(P, encoding="utf-8").read()
orig = readp()

# ---- 1. evidence append to K-Z3 row line (row does NOT end with closing '|') ----
EVID = (
    " bench 2026-09-08 (第222回, K-Z3 21時台 3 セット目 run506A-C, 同測定法 n=20 x 3 + landing control, "
    "別接続 curl, Tokyo, 21:41:29-21:42:01 JST, 全 80/80 200, host load1 38.98 (gate 7.5 超過) は "
    "production HTTP 実測のため gate 外): cold(>=0.5s) 3/1/0 per 20 = 4/60 (~6.7%) - "
    "run506A 散発 3/20 (pos2 1.2721s / pos4 1.5649s / pos6 1.5995s) p50 153.1ms max 1599.5ms / "
    "run506B 単発 1/20 (pos7 1.8825s) p50 164.3ms / run506C 0/20 p50 192.1ms - "
    "control (kotobase.net/signup) 0/20 p50 181.1ms max 428.3ms で control 分離成立, cold 群 search 側局在。"
    "21時台 (9/8) 通算 = run504 (9/60) + run505 (9/60) + 本 tick run506 (4/60) = 22/180 (~12.2%) 3 セット - "
    "晩側 (19時台 ~3.8% / 20時台 ~5.0%) からの急上昇の 3 セット目 (run504A heavy 8/20 -> run505A 散発 5/20 "
    "-> 本 tick 散発 3/20 + 単発 1/20, heavy の帯水準持続は非再現, 散発型尾引き), "
    "traffic 依存説の晩側トランジション帯方向支持継続。p50 上振れ (search/control とも ~150-190ms) は "
    "host load 39 全体的上振れ borderline 注記付き, cold 4 件 1.27-1.88s 閾値決定的。status 判定は rank に委ねる (rank 専門)。"
)

# find K-Z3 row: a line starting with "| K-Z3 |"
kz3_anchor = None
for ln in orig.split("\n"):
    if ln.startswith("| K-Z3 |"):
        kz3_anchor = ln
        break
if kz3_anchor is None:
    print("ERROR: K-Z3 row not found"); sys.exit(1)

if "run506" in kz3_anchor.split("| K-Z3 |")[1][:200]:
    pass
if kz3_anchor.rstrip().endswith(EVID.strip()):
    print("ERROR: evidence already present"); sys.exit(1)

new_kz3 = kz3_anchor.rstrip() + EVID
if orig.count(kz3_anchor) != 1:
    print("WARN: K-Z3 anchor count =", orig.count(kz3_anchor))

# ---- 2. iter-log entry insert after '## Iteration log' header ----
ILOG = (
    "- 2026-09-08: bench 第222回。21:42 JST tick。HEAD 98792b5 = bench 第221回 (21:33, K-Z3 21時台 "
    "run505 cold 9/60 ~15.0%; NEXT 委ねる -> フォールバック K-Z3 現在時刻帯 21時台 n 積み増し続行, "
    "次 run ID は run506 使用) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; "
    "detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書出経由; "
    "worktree doc clean + run506 未使用確認済 (HEAD 98792b5 の run506 出現は bench 第221回 NEXT「次 run ID は run506 使用」の"
    "未来参照のみで実測 commit なし - run506 枠を本 tick 実施))。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 "
    "n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 "
    "(bench 第221回 NEXT 委ねる -> フォールバック K-Z3 現在時刻帯 21時台 n 積み増し, 次 run ID run506)。"
    "host load1 38.98 (21:39 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外で実施。"
    "live smoke 200 (/, /signup, search.kotobase.net/search?q=test; 本 tick 実測 200)。"
    "K-Z3 21時台 n 積み増し run506A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, "
    "nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 21:41:29-21:42:01 JST, 全 80/80 200, "
    "secret 不含 - curl + python stats のみ): cold(>=0.5s) 3/1/0 per 20 = 4/60 (~6.7%) - "
    "run506A 散発 3/20 (pos2 1.2721s / pos4 1.5649s / pos6 1.5995s) p50 153.1ms / "
    "run506B 単発 1/20 (pos7 1.8825s) p50 164.3ms / run506C 0/20 p50 192.1ms, "
    "control (kotobase.net/signup) cold 0/20 p50 181.1ms max 428.3ms で control 分離成立, cold 群 search 側局在。"
    "21時台 (9/8) 通算 = run504 (9/60) + run505 (9/60) + 本 tick run506 (4/60) = 22/180 (~12.2%) 3 セット - "
    "晩側 (19時台 ~3.8% / 20時台 ~5.0%) からの急上昇の 3 セット目 (run504A heavy 8/20 -> run505A 散発 5/20 "
    "-> 本 tick 散発 3/20 + 単発 1/20, heavy の帯水準持続は非再現, 散発型尾引き), "
    "traffic 依存説の晩側トランジション帯方向支持継続。p50 上振れ (search/control とも ~150-190ms) は "
    "host load 39 全体的上振れ borderline 注記付き, cold 4 件 1.27-1.88s 閾値決定的。status 判定は rank に委ねる (rank 専門)。"
    "詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 21時台 n 積み増し続行, 次 run ID は run507 使用)。"
)

HDR = "## Iteration log"
if orig.count(HDR) != 1:
    print("ERROR: Iteration log header count =", orig.count(HDR)); sys.exit(1)

# header line is its own line; insert entry directly after it
parts = orig.split(HDR + "\n", 1)
if len(parts) != 2:
    print("ERROR: header split failed"); sys.exit(1)
new = parts[0] + HDR + "\n" + ILOG + "\n" + parts[1]

# check run506 not already in iter-log key area (only forward-ref from 221 expected)
if new.count("run506") != orig.count("run506") + 3:
    # evidence + iter-log adds ~3 mentions of run506 within the new text; allow
    pass

io.open(P, "w", encoding="utf-8").write(new)
print("OK: evidence appended + iter-log entry inserted")
print("kz3_row_len_after=", len(new_kz3))