import re, subprocess

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

ev = " falsify 2026-09-11 (19:27-19:28 JST tick, K-Z3 19時台 n 積み増し run584A-C, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 全 80/80 200, host load1 28.6-33 (production HTTP 実測のため gate 外), secret 不含 - curl + python3 stats のみ): cold(>=0.5s) 9/2/0 per 20 = 11/60 (~18.3%) - run584A cold 9/20 (0.975-2.203s 散発配置, warm 群と交互) p50 62.6ms max 2.203s / run584B cold 2/20 (1.106s/1.277s) p50 51.3ms / run584C cold 0/20 p50 45.7ms max 65.1ms, control (kotobase.net/signup) cold 1/20 (0.752s 単発) p50 66.0ms max 751.9ms で control に cold 1 件出現し control 分離は borderline not-separated-leaning (search 側 cold 11/60 は閾値決定的だが機構判定としては弱い)。run584A heavy 9/20 は run232A 9/20 型 heavy クラスタに近い規模で B 2/20 が弱く続き A 内即消失型ではない - 19時台通算 (run234 4/60 + run235 6/60 + 本 tick 11/60) = 21/180 (~11.7%) で 18時台 (~7.5%) と 22時台 (~6.0%) を超える夜帯高位方向、ただし control 1 件 + single-run 濃度依存大で帯確定は rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"

# find K-Z3 hypothesis row (starts with | K-Z3 |)
ki = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        ki = i
        break
assert ki is not None, "K-Z3 row not found"
if not lines[ki].rstrip("\n").endswith("\n"):
    pass
lines[ki] = lines[ki].rstrip("\n") + ev + "\n"

# iter-log insertion right after "## Iteration log"
ii = None
for i, l in enumerate(lines):
    if l.startswith("## Iteration log"):
        ii = i
        break
assert ii is not None, "iter log header not found"
entry = ("- 2026-09-11: falsify 第247回 (19:27 JST tick)。HEAD 3ede3dd = fetch 後 net-kotobase/main 先端一致 (worktree detached HEAD, fetch net-kotobase + rev-parse 比較, 乖離 0)。rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は本 tick 時刻 (19時台) のため待機不可能 — フォールバック (production HTTP 実測) で K-Z3 19時台 n 積み増し run584A-C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 19:27:57-19:28:21 JST, 全 80/80 200): cold(>=0.5s) 9/2/0 per 20 = 11/60 (~18.3%) — run584A cold 9/20 (0.975-2.203s 散発配置, run232A 型 heavy クラスタ級) p50 62.6ms / run584B cold 2/20 p50 51.3ms / run584C cold 0/20 p50 45.7ms, control (kotobase.net/signup) cold 1/20 (0.752s) p50 66.0ms で control 分離 borderline not-separated-leaning (cold 11/60 は閾値決定的)。19時台通算 = run234 4/60 + run235 6/60 + 本 tick 11/60 = 21/180 (~11.7%) 夜帯高位方向。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる。secret 不含 (curl + python3 stats のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し、次 run ID は run585 使用)。\n")
lines.insert(ii + 1, entry)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

# combining char scan
text = "".join(lines)
bad = [c for c in text if 0x0300 <= ord(c) <= 0x036F]
print("combining:", len(bad))
print("ev count:", text.count("falsify 2026-09-11 (19:27"))
print("entry count:", text.count("falsify 第247回"))
