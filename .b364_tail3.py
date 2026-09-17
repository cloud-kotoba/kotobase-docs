import io
with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    lines = f.readlines()
l279 = lines[278]
with io.open("/tmp/l279tail.txt", "w", encoding="utf-8") as f:
    f.write("L279[0:40]=" + repr(l279[:40]) + "\n")
    f.write("L279 tail(350)=" + repr(l279[-350:]) + "\n")
    f.write("L279 has newline end: %r\n" % l279.endswith("\n"))
print("ok")