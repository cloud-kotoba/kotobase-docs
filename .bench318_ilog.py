#!/usr/bin/env python3
import io
path = "query-cosientist.md"
data = io.open(path, encoding="utf-8").read()
lines = data.splitlines(keepends=True)

hdr = None
for idx, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr = idx
        break
assert hdr is not None, "iterlog header not found"

entry = (
 "- 2026-09-07: bench 第132回。06:24 JST tick。HEAD bde8c75 = falsify 第146回 (run317A-C, 06:16, "
 "6時台 n-add, cold 0/60 完全静穏 13例目) = remote net-kotobase/main 一致 (fetch + rev-parse, 乖離 0; "
 "worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; "
 "pre-run 計測)。host load1 74.36 (06:22 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し "
 "production HTTP フォールバック (gate 外)。falsify 第146回 NEXT「委ねる (rank 指定優先; フォールバックは "
 "K-Z3 6時台 n-add 継続, 次 run ID run318)」の現時刻帯フォールバック継続として 6時台 n 積み増し "
 "run318A\u2013C を実施 (同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 06:23:28\u201306:24:02 JST, "
 "全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 "
 "\u2014 run318A 0/20 p50 110.6ms / run318B 0/20 p50 115.4ms / run318C 0/20 p50 98.1ms, control 0/20 p50 "
 "104.3ms max 256.0ms (host load 112 high-tick の p50 上振れ borderline note, max 256ms 未満で cold 閾値 "
 "0.5s に達せず 0/60 判定に影響なし)。run318 完全静穏 0/60 は **14 例目** (falsify run317 完全静穏 13例目 "
 "直後の連続再静穏, run283/289/293/296/297/298/303/307/309/312/313/314/317 型), heavy run271A 6/20 型は "
 "run271A 以降 43 セット連続非再現。6時台通算 = falsify run315 (2/60) + bench run316 (1/60) + falsify "
 "run317 (0/60) + 本 tick (0/60) = 3/240 (~1.25%) の 4 セット、deep-night 累計 run275..318 = 43/2640 "
 "(~1.63%) の 44 セットで低位帯水準継続 \u2014 深夜帯\u2192朝の帯境 (6時台) での完全静穏連続 (run317\u2192run318) は "
 "K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる "
 "(rank 専門)。secret は一切記録せず (curl のみ + 統計 python)。NEXT: 委ねる (rank 指定優先; フォールバックは "
 "K-Z3 6時台 n 積み増し継続、次 run ID は run319 使用)。\n"
)
# insert new entry right after header line (position hdr+1)
lines[hdr+1:hdr+1] = [entry]
io.open(path, "w", encoding="utf-8").write("".join(lines))
print("iterlog entry inserted after header (now at line", hdr + 2, ")")
print("verify below header:", repr(lines[hdr+1][:70]))