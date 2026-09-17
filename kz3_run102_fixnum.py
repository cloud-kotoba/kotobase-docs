path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
text = open(path, encoding="utf-8").read()

# Fix 1: evidence line - midnight cumulative denominator and rate
a1 = "4 例目で、深夜帯通算 cold>0 は\n78 試行中 23 試行 (~29%)。"
b1 = "4 例目で、深夜帯通算 cold>0 は\n75 試行中 23 試行 (~31%)。"
assert text.count(a1) == 1, "a1"
text = text.replace(a1, b1)

# Fix 2: evidence NEXT - 0h band is 2/3 trials (102B cold 1/20 counts)
a2 = "NEXT: K-Z3 0時台 n 積み増し継続\n(0時台 3 試行中 1 試行 — 帯発現率の確定には n が不足)。"
b2 = "NEXT: K-Z3 0時台 n 積み増し継続\n(0時台 3 試行中 2 試行 — 帯発現率の確定には n が不足)。"
assert text.count(a2) == 1, "a2"
text = text.replace(a2, b2)

# Fix 3: iteration log - same two corrections
a3 = "(深夜帯通算 cold>0 78 試行中 23 試行 ~29%)。"
b3 = "(深夜帯通算 cold>0 75 試行中 23 試行 ~31%)。"
assert text.count(a3) == 1, "a3"
text = text.replace(a3, b3)

a4 = "NEXT: K-Z3 0時台 n 積み増し継続 (帯発現率 1/3 では確定せず)。"
b4 = "NEXT: K-Z3 0時台 n 積み増し継続 (帯発現率 2/3、確定には n 不足)。"
assert text.count(a4) == 1, "a4"
text = text.replace(a4, b4)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("fixed")
