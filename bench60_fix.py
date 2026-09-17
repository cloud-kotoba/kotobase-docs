import io
# Check whether the append actually happened: the file may have been written by both
# ops in bench60_append.py, but the K-Z3 row update appears to be missing.
# Re-apply just the K-Z3 row addition, idempotently.
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()
lines = src.split("\n")
idx = [i for i, ln in enumerate(lines) if ln.startswith("| K-Z3 | worker |")]
assert len(idx) == 1, idx
row = lines[idx[0]]
if "run174A" in row:
    print("already present")
else:
    addition = (
        " bench 2026-09-05 (第60回, K-Z3 22時台 n 積み増し run174A–C, 同測定法 n=20 × 3 run + landing control, "
        "別接続 curl, Tokyo, 22:49:35–22:49:41 JST, 全 80/80 200, host load1 6.77 は production HTTP 実測のため gate 外): "
        "run174A cold(>=0.5s) 0/20 p50 47ms / run174B cold 1/20 (0.998s, 20番目末尾の単発) p50 39ms / "
        "run174C cold 0/20 p50 47ms (0.033–0.088s) — 合計 1/60, landing control (kotobase.net/, 同時刻, n=20, 全 200) は "
        "cold 0/20 p50 48ms と静穏で control 分離成立 (cold 群は search 側単発, run168/169/173A 型)。"
        "22時台通算は run172 (5/60) + run173 (1/60) + run174 (1/60) = 7/180 (~3.9%) — 21時台 (~58%) より低位、"
        "18–20時台 (~2-3%) と同水準の低位側に更新。status 判定は rank に委ねる"
    )
    # insert before trailing " |"
    assert row.rstrip().endswith("|"), row[-50:]
    body = row.rstrip()
    new_row = body[:-1].rstrip() + " " + addition + " |"
    lines[idx[0]] = new_row
    io.open(path, "w", encoding="utf-8").write("\n".join(lines))
    print("appended to K-Z3 row, line", idx[0] + 1)
