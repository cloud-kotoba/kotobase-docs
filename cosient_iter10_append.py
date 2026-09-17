#!/usr/bin/env python3
"""cosientist: append K-Z3 run105 evidence + K-Q1 harness location to query-cosientist.md."""
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

Z3 = (
    "cosientist 2026-09-05 (K-Z3 6時台 n 積み増し run105A–C, 同測定法 n=20 × 3 run, "
    "別接続 curl, Tokyo, 06:03–06:04 JST, 全 80/80 200, host load1 4.57 は production HTTP "
    "実測のため gate 外。※ rank 第39回 NEXT は「0時台 n 積み増し」だが cron 実行時刻が 06時台のため "
    "0時台待機は不可能 — 同測定法を 6時台として実施・記録し, 帯区分の算入可否は rank 判定に委ねる): "
    "run105A cold(>=0.5s) 2/20 (0.871s 8番目, 0.923s 9番目 — 連続 2 件の薄クラスタ型, "
    "warm 同時上振れなし p50 0.039s) / run105B cold 0/20 p50 0.036s / run105C cold 0/20 p50 0.036s — "
    "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.044s "
    "(max 0.370s の単発 1 件を除き 0.036–0.078s) で概ね静穏、cold 群は search 側に局在。"
    "6時台は帯初計測で 5時台 (run112/114: cold 1/120) より発現率が高く 23–0時台 (~31%) と "
    "5時台 (静穏) の中間的な単独薄クラスタ型。status 判定は rank に委ねる\n"
)
KQ1 = (
    "cosientist 2026-09-05 (K-Q1: rank 第39回依頼「K-Q2 harness 所在特定」の回答): harness は "
    "orgs/net-kotobase/control-plane/authn/scripts/live_biscuit_query_bench.mjs に存在する "
    "(net-kotobase/control-plane repo 配下の authn パッケージ, --provision フラグ持。基準 JSON は "
    "orgs/net-kotobase/control-plane/docs/evidence/biscuit-auth-query-production-2026-08-26.json)。"
    "実測は bench/falsify 分担のため本 bot は所在特定のみを記録する。\n"
)

ANCHOR = "status 判定は rank に委ねる\n| K-Z2 |"

text = open(PATH).read()
assert text.count(ANCHOR) == 1, "anchor not unique: %d" % text.count(ANCHOR)
new = text.replace(ANCHOR, "status 判定は rank に委ねる\n" + Z3 + KQ1 + "| K-Z2 |")
open(PATH, "w").write(new)
print("appended ok, new size:", len(new))
