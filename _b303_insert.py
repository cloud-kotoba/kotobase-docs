#!/usr/bin/env python3
# bench 125: append run303 K-Z3 evidence to hypothesis row line 279 (tail anchor = run302 entry)
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

anchor = "4時台は run300 (1/60) + run301 (1/60) の 2/120 低位帯は維持、run302 の 6/60 は混入のため帯通算に算入しない。deep-night 累計 run275..301 = 32/1620 (~2.0%) の低位帯残界は不変。status 判定は rank に委ねる (rank 専門)。"

# find the line containing the anchor
target_li = None
for i, ln in enumerate(lines):
    if "K-Z3 | worker" in ln and anchor in ln:
        target_li = i
        break
if target_li is None:
    print("ANCHOR_NOT_FOUND")
    raise SystemExit(1)

addition = (
    " bench 2026-09-07 (第125回, K-Z3 4時台 n積み増し run303A–C, 同測定法 n=20 × 3 + landing control, "
    "別接続 curl, Tokyo, 04:23:18–04:23:23 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
    "host load1 42.02 (04:23 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): "
    "cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run303A cold 0/20 p50 45.4ms max 62.0ms / run303B cold 0/20 p50 43.2ms max 55.9ms / "
    "run303C cold 0/20 p50 39.8ms max 59.2ms, control (kotobase.net/signup) cold 0/20 p50 37.7ms max 47.2ms 完全静穏で control 分離成立、"
    "search/control とも 0 cold (完全静穏 0/60 は run283/289/293/296/297/298 型の続きで 7 例目、falsify run302 の not-separated 直後の完全静穏再現)。"
    "4時台は run300 (1/60) + run301 (1/60) + 本 tick run303 (0/60) で 2/180 (~1.1%、run302 6/60 は host 混入のため帯通算に算入しない)、"
    "deep-night 累計 run275..303 = 32/1680 (~1.9%) の 28 セットで低位帯水準継続 — 深夜最低帯 4時台での完全静穏再現は K-Z3 traffic 依存説への反証材料を続行 "
    "(深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる (rank 専門)。"
)

lines[target_li] = lines[target_li].rstrip("\n") + addition + "\n"

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

# verify
with open(path, encoding="utf-8") as f:
    check = f.readlines()
ok = "run303A cold 0/20" in check[target_li] and "完全静穏 0/60" in check[target_li]
print("VERIFY", ok, "line", target_li + 1)