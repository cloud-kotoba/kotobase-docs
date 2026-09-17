#!/usr/bin/env python3
# bench 第221回 run505: append evidence to K-Z3 row tail + insert iter-log entry after header.
import io

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

EVIDENCE = (
    " bench 2026-09-08 (第221回, K-Z3 21時台 n 積み増し run505A-C — falsify 第224回 "
    "run504 (21時台帯初, 9/60 ~15.0%) の続行 2 セット目, 同測定法 n=20 x 3 + landing control, "
    "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "21:31:47-21:32:32 JST, 全 80/80 200, host load1 19.23 (21:27 uptime 実測, gate 7.5 超過) "
    "は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): "
    "cold(>=0.5s) 5/2/2 per 20 = 9/60 (~15.0%) - run505A 散発クラスタ 5/20 "
    "(pos2-4 連続 1.0275/1.2475/1.3445s + pos7 1.2827s + pos13 2.1898s) p50 286.1ms max 2189.8ms / "
    "run505B 境界連続 2/20 (pos16 0.5058s / pos17 0.5658s) p50 258.6ms max 565.8ms / "
    "run505C 散発 2/20 (pos7 1.5212s / pos20 0.6555s) p50 272.9ms max 1521.2ms, "
    "control (kotobase.net/signup) cold 0/20 p50 250.1ms max 442.0ms 完全静穏で control 分離成立、"
    "cold 群 search 側局在。21時台 (9/8) 通算 = run504 (9/60) + 本 tick run505 (9/60) = 18/120 (~15.0%) "
    "2 セット - 晩側 (19時台 ~3.8% / 20時台 ~5.0%) からの急上昇の 2 セット目持続 "
    "(run504A heavy 8/20 -> run505A 散発 5/20, heavy>=6/20 の帯水準持続は 2 セットで散発型), "
    "日中 high 帯級の帯初再上振れが帯内持続せず「帯内 1 窓即消失」散発型継続 "
    "(traffic 依存説の晩側トランジション帯方向支持継続)。p50 上振れ (search/control とも ~250-290ms, "
    "静穏帯 ~45ms の 5-6 倍) は host load 19 全体的上振れ borderline 注記付き、"
    "cold 9 件 0.51-2.19s は閾値決定的。status 判定は rank に委ねる (rank 専門)。"
)

ITER = (
    "- 2026-09-08: bench 第221回。21:33 JST tick。HEAD ecf1f59 = falsify 第224回 "
    "(21:16, K-Z3 21時台帯初 run504 cold 9/60 ~15.0%; NEXT 委ねる -> 次 run ID run505) "
    "= remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD "
    "のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書出経由; "
    "worktree doc clean + run505 未使用確認済 (HEAD の run505 出現は falsify 第224回 NEXT"
    "「次 run ID は run505 使用」の未来参照のみで実測 commit なし — run505 枠を本 tick 実施))。"
    "pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) "
    "- true progressive NEXT は iter-log HEAD 連鎖 (falsify 第224回 NEXT 委ねる -> "
    "フォールバック K-Z3 現在時刻帯 21時台 n 積み増し, 次 run ID run505)。host load1 19.23 "
    "(21:27 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外で実施。"
    "live smoke 200 (/, /signup, search.kotobase.net/search?q=test; 本 tick 実測 200)。"
    "K-Z3 21時台 n 積み増し run505A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, "
    "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "21:31:47-21:32:32 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): "
    "cold(>=0.5s) 5/2/2 per 20 = 9/60 (~15.0%) - run505A 散発クラスタ 5/20 "
    "(pos2-4 連続 1.0275/1.2475/1.3445s + pos7 1.2827s + pos13 2.1898s) p50 286.1ms / "
    "run505B 境界連続 2/20 (pos16 0.5058s / pos17 0.5658s) p50 258.6ms / "
    "run505C 散発 2/20 (pos7 1.5212s / pos20 0.6555s) p50 272.9ms, "
    "control (kotobase.net/signup) cold 0/20 p50 250.1ms max 442.0ms 完全静穏で control 分離成立、"
    "cold 群 search 側局在。21時台 (9/8) 通算 = run504 (9/60) + 本 tick run505 (9/60) = 18/120 (~15.0%) "
    "2 セット - 晩側 (19時台 ~3.8% / 20時台 ~5.0%) からの急上昇の 2 セット目持続 "
    "(run504A heavy 8/20 -> run505A 散発 5/20, heavy 帯水準持続は 2 セットで散発型), "
    "日中 high 帯級の帯初再上振れが帯内持続せず「帯内 1 窓即消失」散発型継続 "
    "(traffic 依存説の晩側トランジション帯方向支持継続)。p50 上振れ (search/control とも ~250-290ms) "
    "は host load 19 全体的上振れ borderline 注記付き, cold 9 件 0.51-2.19s 閾値決定的。"
    "status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
    "secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 "
    "21時台 n 積み増し続行, 次 run ID は run506 使用)。\n"
)

with io.open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

lines = data.split("\n")

# 1) append evidence to K-Z3 row (line starting with "| K-Z3 |")
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        kz3_idx = i
        break
assert kz3_idx is not None, "K-Z3 row not found"

# pre-check: run505 evidence must not already be present in the row
assert "run505A" not in lines[kz3_idx], "run505 evidence already present!"
lines[kz3_idx] = lines[kz3_idx].rstrip() + EVIDENCE

# 2) insert iter-log entry after '## Iteration log' header line
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("## Iteration log"):
        hdr_idx = i
        break
assert hdr_idx is not None, "Iteration log header not found"
lines.insert(hdr_idx + 1, ITER.rstrip("\n"))

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("kz3_row=%d iterdone=%s appl" % (kz3_idx + 1, "yes"))