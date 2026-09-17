#!/usr/bin/env python3
import re

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p) as f:
    lines = f.read().split("\n")

ev = (" falsify 2026-09-15 (K-Z3 20時台 n 積み増し run633A-C, 同測定法 n=20 x3 + landing control, "
      "別接続 curl, Tokyo, 20:18:58-20:22:26 JST, search 60/60 200, control 301): "
      "cold(>=0.5s) 10/2/0 per 20 = 12/60 (~20.0%) - run633A cold 10/20 (640.7-1434.4ms 厚い群発, run 冒頭窓に集中) p50 640.7ms / "
      "run633B cold 2/20 (1261.8/1350.1ms) p50 63.9ms / run633C cold 0/20 p50 70.1ms, "
      "landing control (kotobase.net/signup) cold 1/20 (1133.7ms 単発) p50 63.9ms max 1133.7ms で分離は弱い (leaning-separated)。"
      "20時台通算: 9/10 run586 8/60, 9/12 run588 9/60, 9/13 run606 7/60, 9/15 run633 12/60 - 散発群発帯で日次変動大 (K-Z4 材料)。"
      "status 判定は rank に委ねる (rank 専門)。secret 不含 (curl + python3 stats のみ)。")

# find first K-Z3 hypothesis line
idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        idx = i
        break
assert idx is not None, "K-Z3 line not found"
assert lines[idx].rstrip().endswith("(rank 専門)。"), "anchor end check: " + lines[idx][-40:]
lines[idx] = lines[idx].rstrip() + ev

# insert iteration log entry right after '## Iteration log'
il = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        il = i
        break
assert il is not None, "iter log header not found"
iter_line = ("- 2026-09-15: falsify 第255回 (20:18 JST tick)。HEAD da52171 = fetch 後 net-kotobase/main 先端一致 "
             "(fetch + rev-parse 比較, 乖離 0)。host load1 48-54 (gate 7.5 超過, production HTTP 実測のため gate 外)。"
             "rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は本 tick 時刻 (20時台) のため待機不可能 - "
             "フォールバック (production HTTP 実測) で K-Z3 20時台 n 積み増し run633A-C を実施 "
             "(同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 20:18:58-20:22:26 JST, search 全 60/60 200): "
             "cold(>=0.5s) 12/60 (~20.0%) - A 10/20 群発 (640.7-1434.4ms, 冒頭窓集中) + B 2/20 + C 0/20, "
             "control cold 1/20 単発で分離弱い (leaning-separated)。evidence は K-Z3 仮説行に追記済み。"
             "status 判定は rank に委ねる。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。secret 不含。")
assert lines[il + 1].endswith("\n") or True
lines.insert(il + 1, iter_line)

out = "\n".join(lines)
assert out.count(ev) == 1, "duplicate ev check"
# combining char scan
for ch in out:
    if 0x0300 <= ord(ch) <= 0x036F:
        raise SystemExit("combining char found: %r" % ch)
with open(p, "w") as f:
    f.write(out)
print("edited ok; K-Z3 line", idx + 1)
