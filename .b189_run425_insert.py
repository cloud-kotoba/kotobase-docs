#!/usr/bin/env python3
import io, unicodedata
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = io.open(path, encoding="utf-8").read()
lines = s.split(chr(10))
def scrub(t):
    o = []
    for c in t:
        cat = unicodedata.category(c)
        if cat not in ("Mn", "Cf", "Cc"):
            o.append(c)
    return "".join(o)
ev = scrub(io.open(".b189_run425_ev.txt", encoding="utf-8").read())
ilog = scrub(io.open(".b189_run425_ilog.txt", encoding="utf-8").read())
idx = None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx = i
        break
assert idx is not None
lines[idx] = lines[idx] + ev
news = chr(10).join(lines)
anchor = "## Iteration log" + chr(10)
ia = news.find(anchor)
assert ia != -1
news = news[:ia+len(anchor)] + ilog + news[ia+len(anchor):]
io.open(path, "w", encoding="utf-8").write(news)
io.open(".b189_run425_prev.txt", "w", encoding="utf-8").write("OK %d %d" % (len(ev), len(ilog)))
print("done")