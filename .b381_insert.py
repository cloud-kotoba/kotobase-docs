#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bench 第168回: append K-Z3 run381 evidence + insert iter-log entry.
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Verify anchors
kz3_line_idx = None
ilog_hdr_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |") and kz3_line_idx is None:
        kz3_line_idx = i
    if ln.strip() == "## Iteration log" and ilog_hdr_idx is None:
        ilog_hdr_idx = i

print("kz3_line_idx=%s ilog_hdr_idx=%s" % (kz3_line_idx, ilog_hdr_idx), file=sys.stderr)
if kz3_line_idx is None or ilog_hdr_idx is None:
    print("ANCHOR MISS", file=sys.stderr)
    sys.exit(1)

# newline ensure
if not lines[kz3_line_idx].endswith("\n"):
    lines[kz3_line_idx] += "\n"

evid = (
    " bench 2026-09-07 (第168回, K-Z3 18時台 n-add run381A–C, 同測定法 n=20 × 3 + landing control, "
    "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "18:13:17–18:13:35 JST, 全 80/80 200, host load1 28.6–28.9 (gate 7.5 超過) は production HTTP 実測のため gate 外): "
    "cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run381A cold 単発 1/20 (1.9154s pos20 末尾) p50 137.2ms max 1.915s / "
    "run381B cold 0/20 p50 127.4ms max 248.9ms / run381C cold 単発 1/20 (1.0931s) p50 92.6ms max 1093.1ms, "
    "container control (kotobase.net/signup) cold 0/20 p50 124.1ms max 173.2ms 完全静穏で control 分離成立, "
    "cold 群は search 側に局在。run381A/C 単発 2 件は散発単発型で sibling falsify (in-flight .b380, run ID衝突 — "
    "17hr 既定 run380 の読替予定) と同時帯の独立計測として記録、18時台帯初サンプル cold 2/60 ~3.3% 低位帯候補。"
    "status 判定は rank に委ねる (rank 専門)。秘密 は一切記録せず。"
)
lines[kz3_line_idx] = lines[kz3_line_idx].rstrip("\n") + evid + "\n"

ilog_entry = (
    "- 2026-09-07: bench 第168回。18:13 JST tick。HEAD 367e01c = cosientist 第126回 (17:41, K-Z3 17時台 run380 cold 6/60) = "
    "remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, "
    "fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。"
    "host load1 21.38 (18:07 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
    "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD "
    "(cosientist 第126回, 17:41)「委ねる; フォールバックは K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run381 使用」の run381 枠を本 tick 実施 "
    "(18時台帯初計測, 17時台 run375..380 完了後の帯移行, falsify 第172回 run378 / bench 第167回 run379 / cosientist 第126回 run380 済み)。"
    "ただし本 tick 計測直前に sibling falsify が同 18時台 run380 の in-flight 計測 (.b380_380A/C 等, 18:06 実測) を開始しており 17hr 既定 run380 と "
    "ID 衝突 — 本測は run381 に読替 (run216/run256/run263 precedent, 同一帯 independent 計測として採用可否は rank 判定に委ねる, "
    "衝突注記: 17hr run380 = cosientist canonical, falsify 18hr run380 は別窓 independent 扱い)。"
    "K-Z3 18時台 run381A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
    "正 endpoint search.kotobase.net/search?q=test, 18:13:17–18:13:35 JST, 全 80/80 200, secret 不含 — curl のみ): "
    "cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run381A cold 単発 1/20 (1.9154s pos20) p50 137.2ms / "
    "run381B cold 0/20 p50 127.4ms max 248.9ms / run381C cold 単発 1/20 (1.0931s) p50 92.6ms max 1093.1ms, "
    "control (kotobase.net/signup) cold 0/20 p50 124.1ms max 173.2ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
    "run381A/C 単発 2 件は散発単発型で 18時台帯初 cold 2/60 ~3.3% 低位帯候補 (17時台 sibling 確定分 27/360 ~7.5% と対比し低位帯)。"
    "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し続行、次 run ID は run382 使用)\n"
)
# Insert iter-log entry as first entry after header (before cosientist 第126回)
lines.insert(ilog_hdr_idx + 1, ilog_entry)

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("INSERTED_OK", file=sys.stderr)