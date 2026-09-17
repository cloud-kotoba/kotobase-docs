#!/usr/bin/env python3
# Apply the K-Z3 evidence append (was not applied in the first pass).
import io, sys

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
def readp():
    return io.open(P, encoding="utf-8").read()
orig = readp()

EVID = (
    " bench 2026-09-08 (第222回, K-Z3 21時台 3 セット目 run506A-C, 同測定法 n=20 x 3 + landing control, "
    "別接続 curl, Tokyo, 21:41:29-21:42:01 JST, 全 80/80 200, host load1 38.98 (gate 7.5 超過) は "
    "production HTTP 実測のため gate 外): cold(>=0.5s) 3/1/0 per 20 = 4/60 (~6.7%) - "
    "run506A 散発 3/20 (pos2 1.2721s / pos4 1.5649s / pos6 1.5995s) p50 153.1ms max 1599.5ms / "
    "run506B 単発 1/20 (pos7 1.8825s) p50 164.3ms / run506C 0/20 p50 192.1ms - "
    "control (kotobase.net/signup) 0/20 p50 181.1ms max 428.3ms で control 分離成立, cold 群 search 側局在。"
    "21時台 (9/8) 通算 = run504 (9/60) + run505 (9/60) + 本 tick run506 (4/60) = 22/180 (~12.2%) 3 セット - "
    "晩側 (19時台 ~3.8% / 20時台 ~5.0%) からの急上昇の 3 セット目 (run504A heavy 8/20 -> run505A 散発 5/20 "
    "-> 本 tick 散発 3/20 + 単発 1/20, heavy の帯水準持続は非再現, 散発型尾引き), "
    "traffic 依存説の晩側トランジション帯方向支持継続。p50 上振れ (search/control とも ~150-190ms) は "
    "host load 39 全体的上振れ borderline 注記付き, cold 4 件 1.27-1.88s 閾値決定的。status 判定は rank に委ねる (rank 専門)。"
)

# locate the K-Z3 row exactly (line starting with '| K-Z3 |')
lines = orig.split("\n")
kz3_idx = None
for idx, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        if kz3_idx is not None:
            print("ERROR: multiple K-Z3 rows"); sys.exit(1)
        kz3_idx = idx
if kz3_idx is None:
    print("ERROR: K-Z3 row not found"); sys.exit(1)
row = lines[kz3_idx]
if "run506" in row:
    print("SKIP: run506 already present in K-Z3 row"); sys.exit(0)
if row.rstrip().endswith(EVID.strip()):
    print("SKIP: evidence already applied"); sys.exit(0)

lines[kz3_idx] = row.rstrip() + EVID
io.open(P, "w", encoding="utf-8").write("\n".join(lines))
print("OK: evidence appended to K-Z3 row at line", kz3_idx + 1)
print("run506_in_row:", "run506" in lines[kz3_idx])