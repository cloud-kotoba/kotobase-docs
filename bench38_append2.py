import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

lines = src.split("\n")
idx = [i for i, ln in enumerate(lines) if ln.startswith("| K-Z2 | worker |")]
assert len(idx) == 1, idx
row = lines[idx[0]]

addition = (
    " bench 2026-09-05 (第38回, K-Z2 対比 n 増強 run110/run111, 同測定法 n=20, "
    "別接続 curl, Tokyo, cron */5 発火 04:35:03 JST 直後 fire+~3s 開始と fire+~90s 以降開始, "
    "全 40/40 200, landing control 20/20 200 cold 0 p50 0.043s と静穏, host load1 7.26 "
    "(production HTTP 実測のため gate 外)): direct-after cold 2/20 (0.727s 5番目, 0.802s 2番目) "
    "/ warm 18/20 p50 0.040s / elapsed cold 0/20 p50 0.040s — 本対比は run10/12 型の同方向 "
    "(直後のみ cold → 経過後消失) で、発火直後 vs 経過後の対比は 5 源累計 (run10–15, run52–53, "
    "run106, run107, run110/111) で依然方向非一貫 — 機構確定に至らず。cold 2/20 は薄い cold "
    "クラスタ (warm p50 上振れなし) で run100A/104A/107 型。status 判定は rank に委ねる"
)

assert addition not in row
lines[idx[0]] = row + " " + addition
io.open(path, "w", encoding="utf-8").write("\n".join(lines))
print("appended to K-Z2 row, line", idx[0] + 1)
