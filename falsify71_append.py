import re

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

ev = (" falsify 2026-09-06 (第71回, K-Z3 6時台 n 積み増し run190A–C, 同測定法 n=20 × 3 + landing control,"
      " 別接続 curl, Tokyo, 06:48 JST, 全 80/80 200, host load1 ~100 は production HTTP 実測のため gate 外):"
      " run190A cold(>=0.5s) 0/20 p50 141ms (max 381ms) / run190B cold 0/20 p50 143ms (max 223ms) /"
      " run190C cold 0/20 p50 132ms (max 202ms) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は"
      " cold 0/20 p50 178ms (max 331ms) と静穏で control 分離成立。run186A 群発 (9/20) は 4 tick 連続非再現で"
      " run100A/116A/180A 型「帯内 1 窓即消失」パターンをさらに支持 (本 tick は全 p50 100ms 台と host load 高騰 tick の"
      " 全体的上振れがみられるが cold 濃度判定には影響なし)。status 判定は rank に委ねる (rank 専門)。")

# find the K-Z3 evidence line: last line containing "run189A–C" before the K-Z2 row
idx = None
for i, l in enumerate(lines):
    if "run189A–C" in l and "bench 2026-09-06" in l:
        idx = i
assert idx is not None, "anchor line not found"
assert "| K-Z2 |" not in lines[idx]
lines[idx] = lines[idx].rstrip("\n") + ev + "\n"
with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("appended after line", idx + 1)
