#!/usr/bin/env python3
import io, sys

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
# Header at index 359 (line 360). Insert new newest-first entry at line 361 -> index 360.
entry = (
    "- 2026-09-07: bench 第152回。13:25 JST tick。HEAD f018d56 = rank 第153回 (13:21, fold falsify162 run351 + bench151 run352 -> 13時台 6/120 ~5.0% 2-set, "
    "NEXT run353) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; "
    "terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 20.28 (13:23 uptime 実測, "
    "gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」"
    "は stale (rank 第90回帯 artifact) — true progressive NEXT は rank 第153回 (iter-log 13:21)「K-Z3 13時台 n-add、次 run ID は run353」の run353 枠を本 tick 実施 "
    "(13時台 3 セット目, falsify 第162回 run351 + bench 第151回 run352 済みの積み増し続行)。run353 計測 (同測定法 n=20 x 3 + landing control, 別接続 curl, "
    "cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 13:24:38–13:24:50 JST, 全 80/80 200): cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — "
    "run353A cold 5/20 (0.895s/0.926s/1.161s/0.992s/1.888s 散発クラスタ) p50 92.4ms max 1888.0ms / run353B cold 0/20 p50 58.6ms max 100.3ms / "
    "run353C cold 0/20 p50 55.2ms max 77.5ms, control (kotobase.net/signup) cold 0/20 p50 68.7ms max 482.5ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
    "run353A cold 5/20 散発クラスタは B/C 0/20 + control 0/20 で即消滅し「帯内 1 窓即消滅」継続 (sibling run351 4/20 -> run352 2/20 -> 本 tick run353A 5/20 の "
    "11 分間で 2/20->5/20 への再上振れ, heavy>=6/20 は再達せず run331A 9/20 heavy 型は非再現継続)。13時台 (9/7) 通算 (falsify run351 4/60 + bench run352 2/60 + "
    "本 tick run353 5/60) = 11/180 (~6.1%) の 3 セット中位帯候補。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"
)
lines.insert(360, entry)
newtext = "\n".join(lines)
with io.open(path, "w", encoding="utf-8") as f:
    f.write(newtext)
print("INSERTED iterlog bench 第152回 at line 361, total_lines:", len(lines))