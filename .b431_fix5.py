import io
p = ".b431_runner.py"
t = io.open(p, encoding="utf-8").read()
t = t.replace("\u0301", "")
t = t.replace(", ,", ", ")
t = t.replace(",,", ",")
io.open(p, "w", encoding="utf-8").write(t)
print("OK")
