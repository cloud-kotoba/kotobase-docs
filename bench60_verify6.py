import io
src = io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read()
lines = src.split("\n")
out = []
for i, ln in enumerate(lines):
    if "run174A" in ln:
        out.append("line %d: %.150r ... tail: %.400r" % (i + 1, ln, ln[-400:]))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_verify6.txt", "w", encoding="utf-8").write("\n".join(out) or "none")
