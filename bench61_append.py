import io

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()

idx = s.find("\n| K-Z3 |")
assert idx >= 0
row_start = idx + 1
# end of this table row: next "\n" at start of next line
row_end = s.find("\n", row_start)
row = s[row_start:row_end]
assert row.startswith("| K-Z3 |")
assert row.rstrip().endswith("|")
# evidence column is last cell; insert before trailing " |"
body = row.rstrip()
core = body[:-1].rstrip()  # drop trailing '|', trailing spaces
assert core.endswith("|") is False or True
add = (" bench 2026-09-05 (第61回, K-Z3 23時台 n 積み増し run176A–C "
       "— ※ falsify 第67回 run175A–C (22:59–23:00 JST) と ID 衝突を避け前例 "
       "(run169→170) に従い本分を run176 として記録, 同測定法 n=20 × 3 + landing control, "
       "別接続 curl, Tokyo, 23:43:10–23:43:24 JST, 全 80/80 200, host load1 9.00 は "
       "production HTTP 実測のため gate 外): run176A cold(>=0.5s) 7/20 "
       "(0.929–1.596s, 1–5番目連続クラスタ + 16/17番目の散発, warm p50 56ms) / "
       "run176B cold 0/20 p50 55ms (max 115ms) / run176C cold 0/20 p50 55ms (max 101ms) "
       "— 合計 7/60, landing control (kotobase.net/, 同時刻, n=20, 全 200) は "
       "cold 0/20 p50 58ms max 220ms と静穏で control 分離成立 (search 側 "
       "cold 単独クラスタ, run99A/101A/128A 型の前半クラスタ型, warm 同時上振れなし — "
       "即消失)。23時台 (9/5) 通算は falsify run175 (0/60) + 本 tick (7/60) = 7/120 "
       "(~5.8%) — 9/4 の 23時台 3 例連続クラスタ帯 (~29-32%) からは大きく低下し、"
       "帯レートの日夜差/日差の切分けには追加 n 要。status 判定は rank に委ねる (rank 専門)。")
newrow = core + add + " |"
s = s[:row_start] + newrow + s[row_end:]
open(p, "w", encoding="utf-8").write(s)
print("appended, row len", len(newrow))
