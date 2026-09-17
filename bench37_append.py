import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

lines = src.split("\n")
idx = [i for i, ln in enumerate(lines) if ln.startswith("| K-Z3 | worker |")]
assert len(idx) == 1, idx
row = lines[idx[0]]

addition = (
    " bench 2026-09-05 (第37回, K-Z3 深夜 3時台 n 積み増し run107, 同測定法 n=20, "
    "別接続 curl, Tokyo, 03:33-03:34 JST, 全 20/20 + landing control 20/20 200, "
    "host load1 12.77 (tick 実測 03:30) は production HTTP 実測のため gate 外): "
    "search cold(>=0.5s) 2/20 (0.768s 中盤, 0.954s 2番目 — 散発配置) / warm 18/20 "
    "p50 0.050s (0.037-0.104s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は "
    "cold 0/20 p50 0.050s (0.042-0.073s) と静穏で control 分離成立、cold 群は search 側に局在 "
    "(run104A 型の薄い cold 単独クラスタ, warm p50 上振れなし)。3時台は 1 試行中 1 試行で cold>0、"
    "深夜帯通算は 85 試行中 28 試行 (~32.9%)。traffic 最低帯 (3時台) でも発現が継続しており "
    "traffic 依存説に対する反証材料がさらに増加。status 判定は rank に委ねる"
)

assert not row.endswith(addition)
lines[idx[0]] = row + " " + addition
io.open(path, "w", encoding="utf-8").write("\n".join(lines))
print("appended to K-Z3 row, line", idx[0] + 1)
