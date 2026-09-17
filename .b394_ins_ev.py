#!/usr/bin/env python3
# -*- coding: utf-8 -*-
FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(FN, encoding="utf-8").read()

evidence = " bench 2026-09-07 (第176回, K-Z3 20時台 n 積み増し run394A–C 追加 n-add (run393 は falsify 第168回が先行使用のため run394 に読替, run216/run256/run263/run278 前例 — 20時台 3 セット目, independent 計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:27:21–20:28 JST, 全 80/80 200, host load1 13.30 (20:22 pre-run uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 – curl + python stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) – run394A cold 単発 1/20 (2.4655s pos1 冒頭 1 件) p50 60.2ms max 2.4655s / run394B cold 0/20 p50 57.3ms max 494.1ms / run394C cold 0/20 p50 72.5ms max 168.8ms, control (kotobase.net/signup) cold 0/20 p50 58.1ms max 152.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。run394A 単発 1/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 – falsify run393A 散発 2/20 (20:19) の 8 分後さらに減弱 (heavy 再達せず)。20時台 (9/7) 通算 = bench run392 (7/60) + falsify run393 (2/60) + 本 tick run394 (1/60) = 10/180 (~5.6%) の 3 セット low-to-mid 帯候補 – 19時台 (~8.0%) よりやや低位へ減衰方向 (日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。風向 status 判定は rank に委ねる (rank 専門)。" if False else " bench 2026-09-07 (第176回, K-Z3 20時台 n 積み増し run394A–C 追加 n-add (run393 は falsify 第168回が先行使用のため run394 に読替, run216/run256/run263/run278 前例 — 20時台 3 セット目, independent 計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:27:21–20:28 JST, 全 80/80 200, host load1 13.30 (20:22 pre-run uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 – curl + python stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) – run394A cold 単発 1/20 (2.4655s pos1 冒頭 1 件) p50 60.2ms max 2.4655s / run394B cold 0/20 p50 57.3ms max 494.1ms / run394C cold 0/20 p50 72.5ms max 168.8ms, control (kotobase.net/signup) cold 0/20 p50 58.1ms max 152.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。run394A 単発 1/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 – falsify run393A 散発 2/20 (20:19) の 8 分後さらに減弱 (heavy 再達せず)。20時台 (9/7) 通算 = bench run392 (7/60) + falsify run393 (2/60) + 本 tick run394 (1/60) = 10/180 (~5.6%) の 3 セット low-to-mid 帯候補 – 19時台 (~8.0%) よりやや低位へ減衰方向 (日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"

# anchor: end of falsify run393 evidence in K-Z3 row (unique substring before the row's final <br> or end)
anchor_false = "status 判定は rank に委ねる (rank 専門)。"
# we insert AFTER the falsify run393 text but need uniqueness. Use the run393 tail signature.
ins_point = data.find("run393A 散発 2/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ型継続 – bench run392A heavy 6/20 (20:14) の 5 分後散発減弱で heavy 再達せず (run392A heavy は 1 窓非持続)。")
if ins_point == -1:
    raise SystemExit("ANCHOR1 not found")
# find end of that falsify run393 paragraph: the status sentence that follows
end = data.find("status 判定は rank に委ねる (rank 専門)。", ins_point)
if end == -1:
    raise SystemExit("ANCHOR2 not found")
end += len("status 判定は rank に委ねる (rank 専門)。")
data2 = data[:end] + evidence + data[end:]

with open(FN, "w", encoding="utf-8") as f:
    f.write(data2)
print("inserted evidence ok, marker at", ins_point)