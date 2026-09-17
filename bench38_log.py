import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

assert "run108" in src, "K-Z2 row addition missing?"
assert src.count("run108") == 1, src.count("run108")

marker = "  K-Q1 backend query path 計測を優先)。\n"
assert src.count(marker) == 1, (src.count(marker), "marker count")
entry = (
    "- 2026-09-05: falsify 第38回。新規 evidence: K-Z2 深夜帯 発火直後 vs 経過後 対比 "
    "run108/run109 (04:05 JST, cron */5 発火 04:05:03 直後 fire+3s と fire+~100s, n=20 × 2 + "
    "landing control, 別接続 curl, Tokyo, 全 40/40 200, host load1 4.81 quiet-host)。"
    "direct-after cold 1/20 (0.801s 4番目) / warm 19/20 p50 0.050s — elapsed cold 1/20 "
    "(1.318s 18番目) / warm 19/20 p50 0.038s — 両試行とも単発型で run10/12 型同方向対比は不成立 "
    "(1 組分の反証材料)。landing control 静穏。K-Z3 深夜帯の run100A/104A/107 型薄 cold 単独"
    "クラスタの延長と整合。status 遷移なし (rank 専門)。NEXT: K-Z2 対比の残り n (直後 vs 経過後 "
    "の確定的判定には 3 組以上必要) または rank 指定があればそれを優先。\n"
)
if src.count("- 2026-09-05: falsify 第38回") == 0:
    src = src.replace(marker, marker + entry, 1)
    io.open(path, "w", encoding="utf-8").write(src)
    print("iteration log appended")
else:
    print("already present, skip")
