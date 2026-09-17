import io
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(P, encoding="utf-8") as f:
    txt = f.read()
out = []
# confirm correct glyph present
out.append("閾値 count=%d" % txt.count(u"\u95d0\u5024"))
out.append("乖離 count=%d" % txt.count(u"\u4e56\u96e2"))
idx = txt.find("| K-Z3 |")
row_end = txt.find("\n", idx)
out.append("EV_TAIL_LAST400:")
out.append(txt[row_end-400:row_end])
hidx = txt.find("## Iteration log\n") + len("## Iteration log\n")
out.append("ILOG_FIRST_LAST300:")
out.append(txt[txt.find("NEXT:", txt.find("- 2026-09-08: bench \u7b2c213\u56de")) - 0 : txt.find("\n", txt.find("NEXT:", txt.find("- 2026-09-08: bench \u7b2c213\u56de")))])
with io.open("/tmp/b489_verify2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print("ok")