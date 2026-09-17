import io
p = ".b431_runner.py"
s = io.open(p, encoding="utf-8").read()
s = s.replace('res["C"] = batch("C", SEARCHA,,  ́20,, ".b431_C.txt")', 'res["C"] = batch("C", SEARCHA?,  ́20?, ".b431_C.txt")')
io.open(p, "w", encoding="utf-8").write(s)
print("OK")
