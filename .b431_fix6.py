import io
p = ".b431_stats.py"
s = io.open(p, encoding="utf-8").read()
s = s.replace('"cold"]+', '"cold"]')
io.open(p, "w", encoding="utf-8").write(s)
print("OK", s.count('"cold"]+'))
