import io
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = io.open(PATH, encoding="utf-8").read()
print("run328_count=", txt.count("run328"))
print("falsify150=", txt.count("falsify \u7b2c150\u56de"))
# check K-Z3 row still a single cell (line containing | K-Z3 |)
for i, ln in enumerate(io.open(PATH, encoding="utf-8").readlines()):
    if "| K-Z3 |" in ln:
        print("K-Z3 row line=", i+1)
        break
# iter log insertion
t = io.open(PATH, encoding="utf-8").read()
print("iterlog152=", t.count("\u7b2c152\u56de"))