import io
p = ".b431_ins.py"
t = io.open(p, encoding="utf-8").read()
needle = 'hdr = "## Iteration log"'
fix = 'ev = ev.replace("\\u0301", "")\nit = it.replace("\\u0301", "")\n'
if needle in t and needle not startswith("ev ="):
    t = t.replace(needle, fix + needle, 1)
    io.open(p, "w", encoding="utf-8").write(t)
    print("PATCHED")
else:
    print("NOOP")