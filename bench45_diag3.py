import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()
marker = "NEXT: 委ねる (rank 判断 — 9時台 n 積み増し継続、または K-Q1 engine 内訳の cosientist 実装指定)。\n"
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench45_diag3.txt", "w") as f:
    f.write("count: %d\n" % src.count(marker))
    f.write("count no-newline: %d\n" % src.count(marker.rstrip("\n")))
    f.write("count fragment: %d\n" % src.count("9時台 n 積み増し継続、または K-Q1 engine 内訳の cosientist 実装指定"))
print("done")
