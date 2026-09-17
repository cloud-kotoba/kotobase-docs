lines = open("query-cosientist.md").readlines()
with open("fz160_verify.txt", "w") as f:
    row = lines[211]
    f.write(row[:400] + "\n---TAIL---\n" + row[-250:] + "\n")
    f.write("cols=%d\n" % row.count(" | "))
