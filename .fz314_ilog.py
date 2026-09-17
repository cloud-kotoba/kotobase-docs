#!/usr/bin/env python3
import io

PATH = "query-cosientist.md"
# Insert a new bullet right after the "## Iteration log" header line.
ENTRY = "- 2026-09-07: falsify 第144回。05:46 JST tick。HEAD 89c8848 = rank 第137回 (bench 第130回 run313 を含む fold, HEAD==remote net-kotobase/main 一致, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。rank 第137回 NEXT「K-Z3 current-band(5時台/深夜帯) n-add, 次 run ID run314」の継続枠として自反証 run314 測定を実施。同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 05:45:38\u201305:46 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 24.78 (05:46 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run314A/B/C 全 0/20 (p50 44.4/41.9/41.9ms), control 0/20 (p50 46.2ms max 57.6ms) 完全静穏で control 分離成立。run314 完全静穏 0/60 は run283/289/293/296/297/298/303/307/309/312/313 型の 12 例目 (run312\u2013313\u2013314 の完全静穏 3 連続, 散発単発=即消失の性質を 12 例目で支持), heavy run271A 以降 39 セット非再現。5時台通算 run309(0/60)+run310(2/60)+run311(1/60)+run312(0/60)+run313(0/60)+本 tick run314(0/60) = 3/360 (~0.83%) 6-set, deep-night 累計 run275..314 = 40/2400 (~1.67%) 40-set 低位帯継続 — 深夜帯 5時台での完全静穏 3 連続 (0/60 が 6 セット中 4 セット) は K-Z3 traffic 依存説への反証材料を続行。status 判定・NEXT は rank に委ねる (evidence 追記のみ)。secret は一切記録せず。\n"

lines = io.open(PATH, encoding="utf-8").read().split("\n")
# Find the "## Iteration log" header line.
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr_idx = i
        break
assert hdr_idx is not None, "header not found"
# The next non-empty line after hdr should be a "- 2026-09-07: rank 第137回" bullet.
insert_at = hdr_idx + 1
# check we are inserting before a bullet line
assert lines[insert_at].startswith("- "), lines[insert_at][:60]
lines.insert(insert_at, ENTRY.rstrip("\n"))
open(PATH, "w", encoding="utf-8").write("\n".join(lines))
print(f"OK inserted at line {insert_at+1} (1-based)")
big = open(PATH, encoding="utf-8").read()
print("occur 第144回:", big.count("第144回"))
print("occur run314 12例:", big.count("12 例目"))