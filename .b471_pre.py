p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
raw = open(p, encoding="utf-8").read()
lines = raw.split("\n")
cnt = raw.count("run471")
with open("/tmp/b471_pre.txt", "w", encoding="utf-8") as f:
    f.write("run471_count=%d lines=%d line402_hdr=%r line402_tail=%r\n" % (
        cnt, len(lines), lines[402][:30], lines[402][-60:]))
    # find Iteration log header line
    for i, l in enumerate(lines):
        if l.strip() == "## Iteration log":
            f.write("hdr_line=%d first_entry_after=%r\n" % (i+1, lines[i+1][:40] if i+1 < len(lines) else "EOF"))
            break
print("ok")