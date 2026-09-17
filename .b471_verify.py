p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
raw = open(p, encoding="utf-8").read()
lines = raw.split("\n")
cnt = raw.count("run471")
c472 = raw.count("run472")
with open("/tmp/b471_verify.txt", "w", encoding="utf-8") as f:
    f.write("run471=%d run472=%d lines=%d\n" % (cnt, c472, len(lines)))
    f.write("== L403 tail ==\n")
    f.write(lines[402][-700:] + "\n")
    f.write("== iter-log header block ==\n")
    for i, l in enumerate(lines):
        if l.strip() == "## Iteration log":
            for j in range(i, i+3):
                f.write("L%d: %s\n" % (j+1, lines[j][:160]))
            break
print("ok")