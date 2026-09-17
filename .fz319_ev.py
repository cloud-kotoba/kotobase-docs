p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
print("=== run317/318/319 evidence-line placement (0-based idx) ===")
for i,l in enumerate(lines):
    if ("run317" in l or "run318" in l or "run319" in l or "第146回" in l or "第147回" in l):
        # classify
        tag = "CELL" if i < 357 else "ITERLOG"
        print(i, tag, "start:", l[:35])
print("=== last K-Z3 evidence cell line (idx 356) head ===")
print(repr(lines[356][:80]))
print("=== count total runs in cell region 279..356 ===")
# list first token of each cell line 279..356
for i in range(279, 357):
    tok = lines[i].strip()[:24]
    print(i, tok)