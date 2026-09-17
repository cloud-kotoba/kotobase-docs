import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

lines = src.split("\n")
idx = [i for i, ln in enumerate(lines) if ln.startswith("| K-Z3 | worker |")]
assert len(idx) == 1, idx
row = lines[idx[0]]

addition = (
    " bench 2026-09-05 (第45回, K-Z3 10時台帯初計測 run125A–C, 同測定法 n=20 × 3 + "
    "landing control, 別接続 curl, Tokyo, 10:08 JST, 全 60/60 + control 20/20 200, "
    "host load1 36.0 (tick 実測 10:03) は production HTTP 実測のため gate 外): "
    "run125A cold(>=0.5s) 1/20 (1.042s 薄単発, p50 0.041s), 125B 0/20 (p50 0.037s), "
    "125C 0/20 (p50 0.039s) — 計 1/60 発現。landing control は cold 0/20 (p50 0.040s) "
    "と静穏で control 分離成立。10時台帯初計測は 1/60 と低位 — 9時台 (7/180, run122 突発あり) "
    "に近い水準で 5/6/8/10時台のみ低位という分布の裾の候補を追加 (単一サンプルのため確定はせず、"
    "追加 n 要)。status 判定は rank に委ねる"
)

assert addition not in row
lines[idx[0]] = row + " " + addition
io.open(path, "w", encoding="utf-8").write("\n".join(lines))
print("appended to K-Z3 row, line", idx[0] + 1)
