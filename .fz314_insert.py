#!/usr/bin/env python3
import io

PATH = "query-cosientist.md"
ADDS = " falsify 2026-09-07 (第144回, K-Z3 5時台(深夜帯) n 積み増し run314A\u2013C \u2014 rank 第137回 NEXT\u300cK-Z3 current-band(5時台/深夜帯) n-add\u300dの継続枠 (次 run ID run314), 同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 05:45:38\u201305:46 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 24.78 (05:46 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 \u2014 curl のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 \u2014 run314A cold 0/20 p50 44.4ms max 86.2ms / run314B cold 0/20 p50 41.9ms max 70.7ms / run314C cold 0/20 p50 41.9ms max 54.1ms, control (kotobase.net/signup) cold 0/20 p50 46.2ms max 57.6ms 完全静穏で control 分離成立 (search/control とも 0 cold)。run314 全 0/60 完全静穏で 5時台の完全静穏 0/60 は run283/289/293/296/297/298/303/307/309/312/313 型の 12 例目 (run313 完全静穏直後の連続再静穏 3 連続, 散発単発=即消失の性質を 12 例目で支持, heavy クラスタ run271A 6/20 型は run271A 以降 39 セット連続非再現)。5時台通算 run309 (0/60) + run310 (2/60) + run311 (1/60) + run312 (0/60) + run313 (0/60) + 本 tick run314 (0/60) = 3/360 (~0.83%) 6 セット、deep-night 累計 run275..314 = 40/2400 (~1.67%) 40 セットで低位帯水準継続 \u2014 深夜帯 traffic 最低帯 (5時台) での完全静穏 3 連続 (run312/313/314) 0/60 は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる (rank 専門)。"

lines = io.open(PATH, encoding="utf-8").read().split("\n")
# K-Z3 row is line index 278 (0-based) = line 279 (1-based)
idx = 278
assert lines[idx].lstrip().startswith("| K-Z3 |"), (idx, lines[idx][:80])
old_len = len(lines[idx])
lines[idx] = lines[idx] + ADDS
new_len = len(lines[idx])
open(PATH, "w", encoding="utf-8").write("\n".join(lines))
print(f"OK line279 len {old_len}->{new_len} added multiple-line evidence")
# verify: count occurrences (should remain 1)
big = open(PATH, encoding="utf-8").read()
print("occur run314:", big.count("run314A"))
print("occur 12 例目:", big.count("の 12 例目"))