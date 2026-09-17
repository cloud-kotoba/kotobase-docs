fn = ".b429_insert.py"
s = open(fn, encoding="utf-8").read()
s = s.replace("evo427", "evo429").replace("ilog427", "ilog429")
open(fn, "w", encoding="utf-8").write(s)
print("patched")