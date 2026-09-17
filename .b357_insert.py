#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(path,encoding='utf-8').read().split('\n')

kz3_i=None
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        assert kz3_i is None, f"dup K-Z3 line {i}"
        kz3_i=i
assert kz3_i is not None, "K-Z3 line not found"

# sanity: current tail of K-Z3 line should be run355...14/300
tail=lines[kz3_i][-90:]
print("K-Z3 tail before:", tail)
assert "14/300 (~4.7%)" in tail, "unexpected K-Z3 tail"

kz3_add=(" bench 2026-09-07 (第154回, K-Z3 13時台 n 積み増し run357A–C — iter-log HEAD (bench 第153回, 13:40) NEXT「K-Z3 現在時刻帯 13時台 n 積み増し続行、次 run ID は run356 使用」の run356 枠だが sibling cosientist 第124回 (13:51, .b356 計測 data 未 commit) が同 13時台 run356 を in-flight 先行実施済みのため run357 に読替 (run216/run256/run263/run350 precedent, 13時台 7 セット目の独立計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 13:54:05–13:54:11 JST, 全 80/80 200, host load1 21.54→21.04 (13:54 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run357A cold 0/20 p50 42.8ms max 76.3ms / run357B cold 0/20 p50 47.0ms max 93.0ms / run357C cold 0/20 p50 46.6ms max 119.6ms, control (kotobase.net/signup) cold 0/20 p50 40.9ms max 90.4ms 完全静穏で control 分離成立 (search/control とも 0 cold)。run357 全 0/60 完全静穏は sibling cosientist run356 (5/60, run356A 散発クラスタ 5/20 1.02–1.51s, B/C+control 0/60 即消失) の 3 分後で即減弱し「帯内 1 窓即消失」short-timescale 減弱の再観測 — heavy>=6/20 は再達せず run331A 9/20 heavy 型は非再現継続、13時台で run353A 5/20 → run354A 2/20 → run355A 1/20 → run356A 5/20 → 本 tick 0/60 の散発減弱振幅内)。13時台 (9/7) 通算 = falsify run351 (4/60) + bench run352 (2/60) + bench run353 (5/60) + falsify run354 (2/60) + bench run355 (1/60) + cosientist run356 (5/60) + 本 tick run357 (0/60) = 19/420 (~4.5%) の 7 セット中位帯候補。status 判定は rank に委ねる (rank 専門)。 secret は一切記録せず.")
lines[kz3_i]=lines[kz3_i]+kz3_add

# iterlog: find header, insert entry right after
hdr_i=None
for i,l in enumerate(lines):
    if l.strip()=='## Iteration log':
        hdr_i=i
        break
assert hdr_i is not None, "iterlog header not found"
new_entry=("- 2026-09-07: bench 第154回。13:54 JST tick。HEAD cad715d = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測 + 本 tick 実測全 80/80 200)。host load1 21.54 (13:54 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は bench 第153回 (iter-log, 13:40)「K-Z3 現在時刻帯 13時台 n 積み増し続行、次 run ID は run356 使用」の run356 枠だが sibling cosientist 第124回 (13:51, .b356 計測 data 未 commit) が同 13時台 run356 を in-flight 先行実施済みのため run357 に読替 (run216/run256/run263/run350 precedent, 13時台 7 セット目)。run357 計測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 13:54:05–13:54:11 JST, 全 80/80 200): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run357A cold 0/20 p50 42.8ms max 76.3ms / run357B cold 0/20 p50 47.0ms max 93.0ms / run357C cold 0/20 p50 46.6ms max 119.6ms, control (kotobase.net/signup) cold 0/20 p50 40.9ms max 90.4ms 完全静穏で control 分離成立、cold 群は search 側に局在 (search 側 0/60 のため cold 局在は非適用)。run357 全 0/60 完全静穏は sibling cosientist run356 (5/60, run356A 散発クラスタ 5/20 1.02–1.51s) の 3 分後で即減弱し「帯内 1 窓即消失」短時間スケール減弱を 13時台でも再確認 (heavy>=6/20 は再達せず run331A 9/20 heavy 型は非再現継続)。13時台 (9/7) 通算 = falsify run351 (4/60) + bench run352 (2/60) + bench run353 (5/60) + falsify run354 (2/60) + bench run355 (1/60) + cosientist run356 (5/60) + 本 tick run357 (0/60) = 19/420 (~4.5%) の 7 セット中位帯候補。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 13時台 n 積み増し続行、次 run ID は run358 使用)")
lines.insert(hdr_i+1, new_entry)

open(path,'w',encoding='utf-8').write('\n'.join(lines))
# verify
data=open(path,encoding='utf-8').read()
print("run357A count in K-Z3 line:", data.split('\n')[kz3_i].count("run357"), "run357A:", data.count("run357A"))
print("insert ok, iterlog new head line:", [l[:40] for l in data.split('\n')[hdr_i+1:hdr_i+3]])