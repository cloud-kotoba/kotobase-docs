import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()
assert src.count("run107") == 1
assert src.count("85 試行中 28 試行") == 1
# iteration log entry
marker = "  K-Q1 backend query path 計測を優先)。\n"
assert src.count(marker) == 1
entry = (
    "- 2026-09-05: bench 第37回。新規 evidence: K-Z3 深夜 3時台 run107 (03:33-03:34 JST, "
    "n=20 + landing control, 別接続 curl, Tokyo, 全 40/40 200, host load1 12.77 は "
    "production HTTP 実測のため gate 外)。search cold(>=0.5s) 2/20 (0.768s, 0.954s, 散発) "
    "/ warm 18/20 p50 0.050s — landing control cold 0/20 p50 0.050s と静穏で control 分離成立、"
    "run104A 型の薄い cold 単独クラスタ (warm p50 上振れなし)。3時台 1 試行中 1 試行で cold>0、"
    "深夜帯通算 85 試行中 28 試行 (~32.9%)。traffic 最低帯でも発現継続で traffic 依存説への "
    "反証材料が増加。NEXT (rank 第36回) の K-Z2 発火直後 vs 経過後対比は cron */5 発火時刻 "
    "(3:30/3:35) を tick 途中で cross したため本 tick は K-Z3 側のみ実施。status 遷移なし (rank 専門)。\n"
)
src = src.replace(marker, marker + entry, 1)
io.open(path, "w", encoding="utf-8").write(src)
print("iteration log appended")
