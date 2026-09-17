#!/usr/bin/env python3
p="query-cosientist.md"
s=open(p).read()
lines=s.split("\n")
idx=278  # line 279
l=lines[idx]
add=(" falsify 2026-09-07 (第172回 run378 直後の 17時台 4 セット目積み増しとして bench 第167回 run379 を本 tick 実施 — ただし真の NEXT は rank 第161回/bench 第166回 連鎖の「K-Z3 current-band(17時台) n-add、次 run ID は run378」の読替継続で run378 は falsify 第172回 が先行消費済みのため run379 に読替 (run216/run256/run263/run350 precedent, 17時台 4 セット目の independent 計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 17:55–17:56 JST, 全 80/80 200, host load1 25.36 (17:57 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run379A cold 2/20 冒頭集中ペア (0.6089s pos3 / 0.9061s pos4 連続 2 件) p50 133.5ms max 906.1ms / run379B cold 0/20 p50 67.4ms max 160.3ms / run379C cold 0/20 p50 75.9ms max 152.2ms, control (kotobase.net/signup) cold 0/20 p50 124.4ms max 248.6ms 完全静穏で control 分離成立、cold 群は search 側に局在。run379A 冒頭集中ペア 2/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発型継続 (run377A 7/20 heavy の 16 分後 weak 散発, run378 1/60 に続く低位側へ減衰, heavy>=6/20 は再達せず run368A/373A/377A heavy 型の帯水準持続性は非再現継続)。17時台 (9/7) 通算 = run375 (4/60) + run376 (6/60) + run377 (8/60) + falsify run378 (1/60) + 本 tick run379 (2/60) = 21/300 (~7.0%) の 5 セット中位帯候補 — 16時台 (33/420 ~7.9%) と同水準の日中帯高位方向の帯横断継続 (traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。")
# guard: ensure we don't double-append
marker="bench 第167回 run379"
assert marker not in l, "already appended"
new_l=l+add
lines[idx]=new_l
open(p,"w").write("\n".join(lines))
print("inserted ok, new len L279:", len(new_l))