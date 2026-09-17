import io, sys
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = io.open(p, encoding="utf-8").read()
lines = txt.split("\n")
# find K-Z3 evidence row lines
for i, ln in enumerate(lines, 1):
    if ln.startswith("| K-Z3"):
        print("KZ3ROW_LINE", i, ":", ln)
# find Iteration log header
for i, ln in enumerate(lines, 1):
    if "Iteration log" in ln:
        print("ILOG_HDR_LINE", i, ":", ln)
        print("--- first 5 lines after ---")
        for j in range(i, min(i+6, len(lines))):
            print(j, repr(lines[j]))
        break