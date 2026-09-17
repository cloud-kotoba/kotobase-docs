#!/usr/bin/env python3
import io, sys
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx = i
        break
if idx is None:
    sys.exit("KZ3_ROW_NOT_FOUND")

suffix = (
    " cosientist 第147回 (18:11:31 JST 窓, 18時台 n-add run491 — run489/490 は bench 第213回/falsify 第219回先行のため読替, "
    "同測定法 n=20 × 3 全 60/60 200 + landing control 20/20 200, host load1 185.37 (gate 外) p50 上振れ込み): "
    "cold(>=0.5s) 6/60 (~10.0%) — run491A 3/20 (1.2076/1.5819/1.7001s 散発) / run491C 3/20 (0.5148/0.6980/0.7167s 薄散発), "
    "B 0/20, landing control cold 1/20 (1.2771s) で control 分離 borderline not-separated 傾向 (search 6 件 0.51-1.70s 閾値決定的). "
    "18時台 (9/8) 通算 = run489 (7/60) + run490 (7/60) + run491 (6/60) = 20/180 (~11.1%) の 3 セット日中帯高位継続, "
    "17時台 (28/240 ~11.7%) に続く高位帯で traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変. "
    "status 判定は rank に委ねる (rank 専門)."
)
lines[idx] = lines[idx] + suffix
with io.open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("EVAPPEND_OK")