#!/usr/bin/env python3
import io
PATH = "/tmp/bench318.raw"
rows = {}
for ln in io.open(PATH, encoding="utf-8"):
    p = ln.split()
    if len(p) < 4 or p[3] != "200":
        continue
    rows.setdefault(p[0], []).append(float(p[2]))

def cold_count(v):
    return sum(1 for x in v if x >= 0.5)

def p50(v):
    s = sorted(v)
    n = len(s)
    return s[n//2] if n % 2 else (s[n//2-1]+s[n//2])/2

for lbl in ["A", "B", "C", "CTRL"]:
    v = rows.get(lbl, [])
    if not v:
        print(f"{lbl}: NO DATA")
        continue
    colds = sorted([x for x in v if x >= 0.5])
    coldinfo = " ".join(f"{i+1}:{x*1000:.0f}ms" for i, x in enumerate(v) if x >= 0.5)
    print(f"{lbl}: n={len(v)} cold={cold_count(v)}/20 p50={p50(v)*1000:.1f}ms max={max(v)*1000:.1f}ms")
    if coldinfo:
        print(f"  cold positions: {colds}, idx: {coldinfo}")