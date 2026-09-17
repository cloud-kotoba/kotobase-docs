import io
for fn in [".b429_runner.sh", ".b429_stats.py"]:
    s = open(fn, encoding="utf-8").read()
    s = s.replace(".b427_", ".b429_").replace("run427", "run429")
    open(fn, "w", encoding="utf-8").write(s)
    print(fn, "patched")