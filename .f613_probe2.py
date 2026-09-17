lines = open("query-cosientist.md", encoding="utf-8").read().split("\n")
for n, l in enumerate(lines):
    if l.startswith("| K-Z3 |") or l.startswith(" bench 2026-09-14") or l.startswith(" bench 2026-09-13"):
        print(n, repr(l[:60]), "END:", repr(l[-60:]))
