#!/usr/bin/env python3
# -*- coding: utf-8 -*-
SRC = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(SRC, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find "## Iteration log" header line index
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        hdr_idx = i
        break
assert hdr_idx is not None, "iterlog header not found"

entry = (
    "- 2026-09-07: bench 第110回。00:39 JST tick。HEAD 19a576a = remote net-kotobase/main 一致 "
    "(worktree detached HEAD, fetch + rev-parse 比較, 乖離 0)。live smoke 200 (/, /signup; pre-run 計測)。"
    "host load1 27.92→27.35 (00:37→00:39 uptime 実測, gate 7.5 大幅超過) のため local 測定を拒否し "
    "production HTTP フォールバック (gate 外)。rank 第119回 NEXT「K-Z3 24時台(0時台) n 積み増し継続"
    "(次 run ID は run272 使用)」に従い 現時刻帯 0時台(24時台) n 積み増し run272A\u2013C を実施 "
    "(同測定法 n=20 × 3 + landing control, 別接続 curl, 00:39:07\u201300:39:1x JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) "
    "\u2014 run272A cold 2/20 (1.16s / 1.43s 散発配置, warm 群 0.050\u20130.205s で交互) p50 0.051s "
    "/ run272B cold 0/20 p50 0.049s max 0.100s / run272C cold 0/20 p50 0.046s max 0.063s, "
    "control (kotobase.net/signup) cold 0/20 p50 0.042s max 0.059s 完全静穏で control 分離成立、"
    "cold 群は search 側に局在。run272A cold 2/20 は B/C 0/20 即消失で「帯内 1 窓即消失」散発単発/ペア型"
    "(run269A 3/20 散発減弱\u2192run271A 6/20 heavy 再上振れの振幅内の低め位置)、24時台通算 "
    "(run268 2/60 + run269 3/60 + run270 1/60 + run271 7/60 + 本 tick 2/60) = 15/300 (~5.0%) の "
    "5 セット連続 cold>0 で K-Z3 traffic 依存説への反証材料を継続 (深夜帯 traffic 最低帯での cold "
    "連続出現、深夜帯 ~26\u201331% 平坦パターンと整合方向)。status 判定は rank に委ねる (rank 専門)。"
    "secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; "
    "フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run273 使用)。\n"
)

# insert right after the header line
lines.insert(hdr_idx + 1, entry)
with open(SRC, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("inserted bench iterlog entry after header (index", hdr_idx + 1, ")")
print("new total lines:", len(lines))