p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
L = lines[278]
print("L278 LEN", len(L))
for k in ["run317","run318","run319","第146回","第138回","取込 判定"]:
    print(k, "count in L278:", L.count(k))
# tail of L278
print("...L278 tail 400:", L[-400:])
# What is idx 356-357 after current HEAD?
for k in range(354,358):
    print("idx",k,"len",len(lines[k]))
# check bench133 evidence placement - does bench133 run319 appear in cell? 
print("run319 count in cell (279-356):", sum(1 for i in range(279,357) if "run319" in lines[i]))
print("has bench 第1xx回 fold note lines in cell? examples ' rank 第'")
for i in range(279,357):
    if lines[i].strip().startswith("rank 第") or lines[i].strip().startswith("取込"):
        print("  cell fold @", i, ":", lines[i][:40])