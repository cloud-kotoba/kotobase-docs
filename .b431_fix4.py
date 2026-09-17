import io
p = ".b431_runner.py"
t = io.open(p, encoding="utf-8").read()
t = "".join(ch for ch in t if not (0x300 <= ord(ch) <= 0x36F) and ch != "\u02dc") or ch == "\n" or ch == "\t" or 32 <= ord(ch) <= 126)
t = t.replace(", ,",", ,").replace(",,",",")
io.open(p, "w", encoding="utf-8").write(t)
print("OK len=", len(t))
