#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
marker = "## Iteration log"
note = (
    "bench 2026-09-06 (第91回, K-Z3 16時台 n 積み増し run222A\u2013C, 同測定法 n=20 \u00d7 3 + landing control, "
    "別接続 curl, Tokyo, 16:09:49 JST, 全 80/80 200, host load1 9.43 (pre-run 実測, gate 7.5 超過) は production HTTP 実測のため gate 外): "
    "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) \u2014 run222A 冒頭単発 1.182s (1番目, 散発型) p50 42.3ms (min 34.6ms), "
    "run222B 0/20 p50 41.9ms (max 72.4ms) / run222C 0/20 p50 44.1ms (max 65.0ms), "
    "landing control (kotobase.net/signup) cold 0/20 p50 46.0ms max 255ms (単発 1 件 0.255s) 静穏で control 分離成立、cold 群は search 側に局在。"
    "run222A 冒頭単発は B/C 0/20 で即消失し run216/217/218/219/220 型「帯内 1 窓即消失」パターンと整合 (falsify 第93回 run221 0/60 完全静穏の 7 分後の弱い再現)。"
    "16時台通算 本日分 (run221 0/60 + 本 tick 1/60) 1/120 の低位帯サンプル \u2014 日差込みの帯確定には追加 n 要。"
    "status 判定は rank に委ねる (rank 専門)。\n"
)
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
assert content.count(marker) == 1, f"marker count={content.count(marker)}"
content = content.replace(marker, note + marker, 1)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("inserted ok")