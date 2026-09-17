#!/usr/bin/env python3
import io

path = "query-cosientist.md"
s = open(path, encoding="utf-8").read()

# ---- 1. Append run350 evidence to K-Z3 evidence field (L279, unique tail anchor) ----
# anchor: the unique end of the run348 evidence entry on L279
tail_anchor = "12時台 (9/7) 通算 = run345 9/60 + run346 3/60 + run347 6/60 + 本 tick run348 0/60 = 18/240 (~7.5%) 4 セット。status 判定は rank に委ねる (rank 専門)。"
assert s.count(tail_anchor) == 1, f"tail anchor count={s.count(tail_anchor)}"

new_ev = " bench 2026-09-07 (第150回, K-Z3 12時台 n 積み増し run350A–C — rank 第151回 NEXT「K-Z3 12時台 n-add 継続、次 run ID は run349 使用」の run349 枠だが sibling cosientist が同 12時台 run349 を 12:48 in-flight (未 commit, .b349 runner/data を確認) のため run350 に読替 (run216/run256/run263 precedent 独立 2 計測, 採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 12:57:46–12:57:56 JST, 全 80/80 200, host load1 23.53–25.54 (12:57 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run350A cold 3/20 散発クラスタ (1.5014s/1.0516s/1.1273s) p50 72.3ms / run350B cold 0/20 p50 64.3ms max 92.4ms / run350C cold 0/20 p50 41.7ms max 58.9ms, control (kotobase.net/signup) cold 0/20 p50 45.0ms max 129.7ms 完全静穏で control 分離成立、cold 群は search 側に局在。run350A cold 3/20 は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ継続 (sibling run347A heavy 6/20 の ~20 分後弱い再出現, heavy>=6/20 は再達せず run331A 9/20 heavy 型は非再現継続)。12時台 (9/7) 通算 = run345 9/60 + run346 3/60 + run347 6/60 + run348 0/60 + 本 tick run350 3/60 = 21/300 (~7.0%) 5 セット中位帯。status 判定は rank に委ねる (rank 専門)。"

s = s.replace(tail_anchor, tail_anchor + new_ev, 1)

# ---- 2. Insert bench 第150回 iterlog entry at head, right after "## Iteration log" ----
hdr = "## Iteration log\n"
assert s.count(hdr) == 1, f"iterlog hdr count={s.count(hdr)}"

new_entry = (
    "- 2026-09-07: bench 第150回。12:58 JST tick。HEAD 65537a1 = rank 第151回 (12:52, fold falsify161 run347 + bench149 run348, NEXT run349) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 23.95 (12:56 pre-run) → 23.5–25.5 (12:57 測定時, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は rank 第151回 (Iteration log 先頭, 12:52)「K-Z3 12時台 n-add 継続、次 run ID は run349 使用」の run349 枠だが sibling cosientist が同 12時台 run349 を 12:48 in-flight 先行実施 (runner/計測 data .b349 未 commit を確認) のため run350 に読替 (run216/run256/run263 precedent, 12時台 5 セット目の独立計測として採用可否は rank 判定に委ねる)。run350 計測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 12:57:46–12:57:56 JST, 全 80/80 200): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run350A cold 3/20 散発クラスタ (1.5014s/1.0516s/1.1273s) p50 72.3ms / run350B cold 0/20 p50 64.3ms max 92.4ms / run350C cold 0/20 p50 41.7ms max 58.9ms, control (kotobase.net/signup) cold 0/20 p50 45.0ms max 129.7ms 完全静穏で control 分離成立、cold 群は search 側に局在。12時台 (9/7) 通算 = run345 9/60 + run346 3/60 + run347 6/60 + run348 0/60 + 本 tick run350 3/60 = 21/300 (~7.0%) 5 セット中位帯。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。\n"
)

s = s.replace(hdr, hdr + new_entry, 1)

open(path, "w", encoding="utf-8").write(s)
print("write done")
print("run350 count:", s.count("run350"))
print("iter entry count:", s.count("bench 第150回"))