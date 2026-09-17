import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

lines = src.split("\n")
idx = [i for i, ln in enumerate(lines) if ln.startswith("| K-Z2 | worker |")]
assert len(idx) == 1, idx
row = lines[idx[0]]

addition = (
    " falsify 2026-09-05 (深夜帯 発火直後 vs 経過後 対比 run108/run109, 同測定法 n=20, "
    "別接続 curl, Tokyo, cron */5 発火 04:05:03 JST 直後 fire+3s 開始と fire+~100s 以降開始, "
    "全 40/40 200, landing control 200 ttfb 0.040s と静穏, host load1 4.81 (quiet-host, "
    "production HTTP 実測のため gate 外)): direct-after (fire+3s) cold 1/20 (0.801s, 4番目) "
    "/ warm 19/20 p50 0.050s / elapsed (fire+~100s) cold 1/20 (1.318s, 18番目) / warm 19/20 "
    "p50 0.038s — 両試行とも単発型 cold 1 件で run10/12 型の「直後のみ cold 群 → 経過後 0」の "
    "同方向対比は不成立 (9/4 11時台 3 組中 2 組の対比と反し 1 組分の反証材料)。cold は深夜帯の "
    "薄い cold 単独クラスタ (run100A/104A/107 型) の延長と整合し warm p50 上振れなし。"
    "status 判定は rank に委ねる"
)

assert not row.endswith(addition)
lines[idx[0]] = row + " " + addition
io.open(path, "w", encoding="utf-8").write("\n".join(lines))
print("appended to K-Z2 row, line", idx[0] + 1)

# iteration log entry
marker = "  K-Q1 backend query path 計測を優先)。\\n"
if src.count(marker) != 1:
    # fallback: append after the bench 第37回 entry
    marker = "status 遷移なし (rank 専門)。\\n"
    cnt = src.count(marker)
    assert cnt >= 1, "no marker"
entry = (
    "- 2026-09-05: falsify 第38回。新規 evidence: K-Z2 深夜帯 発火直後 vs 経過後 対比 "
    "run108/run109 (04:05 JST, cron */5 発火 04:05:03 直後 fire+3s と fire+~100s, n=20 × 2 + "
    "landing control, 別接続 curl, Tokyo, 全 40/40 200, host load1 4.81 quiet-host)。"
    "direct-after cold 1/20 (0.801s 4番目) / warm 19/20 p50 0.050s — elapsed cold 1/20 "
    "(1.318s 18番目) / warm 19/20 p50 0.038s — 両試行とも単発型で run10/12 型同方向対比は不成立 "
    "(1 組分の反証材料)。landing control 静穏。K-Z3 深夜帯の run100A/104A/107 型薄 cold 単独"
    "クラスタの延長と整合。status 遷移なし (rank 専門)。NEXT: K-Z2 対比の残り n (直後 vs 経過後 "
    "の確定的判定には 3 組以上必要) または rank 指定があればそれを優先。\\n"
)
src = io.open(path, encoding="utf-8").read()
assert src.count(marker) == 1, (marker, src.count(marker))
src = src.replace(marker, marker + entry, 1)
io.open(path, "w", encoding="utf-8").write(src)
print("iteration log appended")
