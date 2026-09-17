#!/usr/bin/env python3
import subprocess, difflib

head = subprocess.run(["git", "show", "HEAD:query-cosientist.md"], capture_output=True, text=True).stdout
wt = open("query-cosientist.md").read()

def kz3_lines(s):
    out = []
    for i, line in enumerate(s.splitlines(), 1):
        if line.startswith("| K-Z3 "):
            out.append((i, line))
    return out

h = kz3_lines(head)
w = kz3_lines(wt)
print("HEAD K-Z3 rows:", [i for i, _ in h])
print("WT   K-Z3 rows:", [i for i, _ in w])

if h and w:
    hl = h[0][1]
    wl = w[0][1]
    print("same:", hl == wl)
    if hl != wl:
        # find common prefix/suffix
        sm = difflib.SequenceMatcher(None, hl, wl)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            print(f"--- {tag} HEAD[{i1}:{i2}] ({i2-i1} chars):")
            print(repr(hl[i1:i2][:800]))
            print(f"+++ {tag} WT[{j1}:{j2}] ({j2-j1} chars):")
            print(repr(wl[j1:j2][:800]))

# also check other differing lines
hl_all = head.splitlines()
wl_all = wt.splitlines()
print("total lines head/wt:", len(hl_all), len(wl_all))
import itertools
ndiff = 0
for i, (a, b) in enumerate(itertools.zip_longest(hl_all, wl_all), 1):
    if a != b:
        ndiff += 1
        if ndiff <= 10:
            print(f"L{i}: HEAD={a[:120]!r}")
            print(f"L{i}: WT  ={b[:120]!r}")
print("diff lines total:", ndiff)
