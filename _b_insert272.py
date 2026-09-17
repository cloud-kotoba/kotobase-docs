#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Insert bench run272 evidence entry as a new physical line after line 268 (run271 entry),
# within the K-Z3 evidence cell (the cell wraps across physical lines 261-272+).
# bench is permitted to append to the evidence cell of the hypothesis row only.
SRC = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(SRC, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# sanity: line 268 (index 267) is the run271 entry
assert 'run271A-C' in lines[267], "line 268 not run271 entry"

new_entry = (
    "bench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A\u2013C \u2014 "
    "rank 第119回 NEXT\u300cK-Z3 24時台(0時台) n 積み増し継続 (次 run ID は run272 使用)\u300dに従い"
    "現時刻帯 0時台(24時台) n 積み増しを実施 (同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, "
    "00:39 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
    "host load1 27.92\u219227.35 (00:37\u219200:39 uptime 実測, gate 7.5 大幅超過) は "
    "production HTTP 実測のため gate 外): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) \u2014 "
    "run272A cold 2/20 (1.16s / 1.43s 散発配置, warm 群 0.050\u20130.205s で cold と交互) p50 0.051s "
    "/ run272B cold 0/20 p50 0.049s max 0.100s / run272C cold 0/20 p50 0.046s max 0.063s, "
    "control (kotobase.net/signup) cold 0/20 p50 0.042s max 0.059s 完全静穏で control 分離成立、"
    "cold 群は search 側に局在。run272A cold 2/20 は B/C 0/20 + control 0/20 で即消失し"
    "\u300c帯内 1 窓即消失\u300d散発単発/ペア型継続 (run269A 3/20 から run270A 1/20 散発減弱\u2192"
    "run271A 6/20 heavy 再上振れの振幅内の低め位置) — 24時台通算 (run268 2/60 + run269 3/60 + "
    "run270 1/60 + run271 7/60 + 本 tick 2/60) = 15/300 (~5.0%) の 5 セット連続 cold>0 で "
    "K-Z3 traffic 依存説への反証材料を継続 (深夜帯 24/0時台 traffic 最低帯での cold 連続出現、"
    "深夜帯 ~26\u201331% 平坦パターンと整合方向)。ただし全セット\u300c帯内 1 窓即消失\u300d型で "
    "帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門).\n"
)

lines.insert(268, new_entry)

with open(SRC, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("inserted run272 entry after line 268 (index 267)")
print("new line count:", len(lines))