import io
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
dst = "/tmp/b489_verify.txt"
with io.open(P, encoding="utf-8") as f:
    txt = f.read()
out = []
idx = txt.find("| K-Z3 |")
row_start = txt.find("\n", idx)  # end of the | K-Z3 | ... opening line? no: row spans lines
# K-Z3 row is a single physical line ending at its newline
row_end = txt.find("\n", idx)
row = txt[idx:row_end]
out.append("EV_TAIL600:")
out.append(row[-600:])
hdr = "## Iteration log\n"
hidx = txt.find(hdr) + len(hdr)
out.append("ILOG_HEAD:")
out.append(txt[hidx:hidx+1100])
with io.open(dst, "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print("verify_written")