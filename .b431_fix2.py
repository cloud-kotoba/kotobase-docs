import io
p = ".b431_runner.py"
t = io.open(p, encoding="utf-8").read()
t = t.replace("math.ceil(0.5 * len(s)) - 1]", "math.ceil(0.5 * len(s)) - 1)]")
io.open(p, "w", encoding="utf-8").write(t)
print("OK")
