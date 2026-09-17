import io
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
p = base + "/query-cosientist.md"
evp = base + "/.b485_ev.txt"
with io.open(p, encoding="utf-8") as f:
    lines = f.readlines()
ial = 279 - 1            # 0-based index of physical line 279
l279 = lines[ial]
assert l279.startswith("| K-Z3 |"), "L279 not K-Z3: " + l279[:20]
with io.open(evp, encoding="utf-8") as f:
    ev = f.read().strip()
clean = []
for ch in ev:
    cp = ord(ch)
    if 0x200B <= cp <= 0x200F:
        continue
    if ch in "\r\n\x0b\x0c":
        continue
    clean.append(ch)
ev = "".join(clean).strip()
lines[ial] = l279.rstrip("\n") + " " + ev + "\n"
with io.open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("ok L279 len", len(lines[ial]))