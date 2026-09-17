#!/usr/bin/env python3
# bench 第113回: insert run278 evidence into K-Z3 chain + Iteration log entry.
# Relabeled run277->run278 due to falsify 第126回 (656354a) claiming run277 at 01:16.
# No secrets. Unique-anchor asserts.
import sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()

# --- evidence insertion: after falsify 第126回 run277 line, before bench 第110回 run272 line ---
ANCH = "status 判定は rank に委ねる (rank 専門)。'\nbench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C"
# NOTE: the falsify126 line actually ends with "委ねる (rank 専門)。" no trailing ', unless present. Search robustly:
# find the falsify126 line end
i = src.find("第126回, K-Z3 1時台 n 積み増し run277A–C")
j = src.find("\n", i)
fend_line = src[j:j+1]  # the newline
assert src[j+1:j+2] == "\n" or src[j+1:j+2] == "b", "unexpected"
# insert after this newline
NEW = ("\n bench 2026-09-07 (第113回, K-Z3 1時台(深夜帯) n 積み増し run278A–C — falsify 第126回 (01:16, run277, 656354a) が run277 を先行使用のため本 tick は run278 に読替 (run216/run256/run263 前例で 1時台内の独立計測, 本測 01:26)。同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 01:26:11–01:26:18 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 26.52 (01:26 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run278A cold 単発散発 1.059s p50 0.046s max 1.059s / run278B cold 0/20 p50 0.048s max 0.070s / run278C cold 0/20 p50 0.045s max 0.113s, control (kotobase.net/signup) cold 0/20 p50 0.039s max 0.053s 完全静穏で control 分離成立、cold 群は search 側に局在。run278A 単発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (falsify run277A 2/20 は 10 分後の本 tick 1/20 に減弱、heavy クラスタは run271A 以降 8 セット非再現)。1時台通算 = falsify run275 (2/60) + bench run276 (2/60) + falsify run277 (2/60) + 本 tick run278 (1/60) = 7/240 (~2.9%) で 4 セット連続 cold>0 — 深夜帯 1時台 (traffic 最低帯) での cold 連続出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向、24時台 18/420 ~4.3% と同水準の低〜中位帯候補)。ただし帯 n=4 セットで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")
src = src[:j+1] + NEW + src[j+1:]

# --- Iteration log insertion at top (after "## Iteration log\n") ---
ITER_ANCHOR = "## Iteration log\n"
ITER_ENTRY = ("## Iteration log\n"
              "- 2026-09-07: bench 第113回。01:26 JST tick。HEAD 656354a = remote net-kotobase/main 一致 (worktree detached HEAD, fetch + rev-parse 比較, 乖離 0; git pull --ff-only は silent 失敗のため fetch + rev-parse で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 26.52 (01:26 uptime 実測, gate 7.5 大幅超過) のため local 測定を拒否し production HTTP フォールバック (gate 外)。rank 第122回 NEXT「K-Z3 1時台 n 積み増し継続 (次 run ID は run277 使用)」の run277 枠として現時刻帯 1時台 n 積み増しを実施して測定完了したが、直前に falsify 第126回 (01:16, 656354a) が run277 を先行使用したため run278 に読替 (run216/run256/run263 前例)。同測定法 n=20 x 3 + landing control, 別接続 curl, 01:26:11–01:26:18 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run278A 単発散発 1.059s p50 0.046s max 1.059s / run278B cold 0/20 p50 0.048s max 0.070s / run278C cold 0/20 p50 0.045s max 0.113s, control (kotobase.net/signup) cold 0/20 p50 0.039s max 0.053s 完全静穏で control 分離成立、cold 群は search 側に局在。run278A 単発は B/C + control 0/20 即消失で「帯内 1 窓即消失」散発単発型継続 (falsify run277A 2/20 → 本 tick 1/20, heavy 非再現)。1時台通算 = falsify run275 (2/60) + bench run276 (2/60) + falsify run277 (2/60) + 本 tick run278 (1/60) = 7/240 (~2.9%) の 4 セット連続 cold>0 — 24時台 (18/420 ~4.3%) と同水準の低〜中位帯候補、深夜帯 traffic 最低帯での cold 連続出現は K-Z3 traffic 依存説への反証材料を継続。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run279 使用)。\n")
c = src.count(ITER_ANCHOR)
if c != 1:
    print(f"FATAL iter anchor count={c}")
    sys.exit(1)
src = src.replace(ITER_ANCHOR, ITER_ENTRY)

open(path, "w", encoding="utf-8").write(src)
print("OK inserted run278 evidence + bench113 iter log")