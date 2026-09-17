import io, traceback

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
logpath = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank48_edit_log.txt"
lines = []
try:
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    i = text.find("rank (期待 gain")
    j = text.find("2. K-Z2", i)
    lines.append("rank idx=%d z2 idx=%d" % (i, j))
    lines.append(repr(text[i:i+2400]))
    with io.open(logpath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
except Exception:
    with io.open(logpath, "w", encoding="utf-8") as f:
        f.write(traceback.format_exc())
