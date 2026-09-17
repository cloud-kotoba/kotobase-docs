import glob

for p in sorted(glob.glob(".b573_*.ttfb")):
    with open(p, encoding="utf-8") as f:
        raw = f.read()
    lines = [l for l in raw.split("\n")]
    bad = [l for l in lines if l.strip() and len(l.split()) != 2]
    print(p, "bytes=", len(raw), "lines=", len([l for l in lines if l.strip()]), "bad=", len(bad))
    for b in bad[:3]:
        print("  BAD:", repr(b))
    with open(p + ".first", "w", encoding="utf-8") as f:
        f.write("\n".join(lines[:3]))
