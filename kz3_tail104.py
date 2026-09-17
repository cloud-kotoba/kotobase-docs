lines = open("query-cosientist.md", encoding="utf-8").read().splitlines()
with open("kz3_tail104.txt", "w", encoding="utf-8") as f:
    for i, ln in enumerate(lines[-30:], start=len(lines) - 29):
        f.write("%d|%s\n" % (i, ln))
print("ok")
