import io
p = ".b431_runner.py"
lines = io.open(p, encoding="utf-8").readlines()
for i, l in enumerate(lines):
    o = l.count("(")
    c = l.count(")")
    if o != c:
        print(i + 1, "open", o, "close", c, l.rstrip()[:85])
