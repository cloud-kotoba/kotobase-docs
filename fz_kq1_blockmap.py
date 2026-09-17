#!/usr/bin/env python3
path = "query-cosientist.md"
lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
idx = None
for i, line in enumerate(lines):
    if line.startswith("| K-Q1 "):
        idx = i
        break
assert idx is not None
end = None
for j in range(idx + 1, len(lines)):
    if lines[j].startswith("| K-"):
        end = j
        break
assert end is not None
for k in range(idx, end):
    ln = lines[k].rstrip("\n")
    print(f"L{k+1} (len {len(ln)}) endswith_pipe={ln.endswith('|')} tail={ln[-60:]!r}")
print("<<END>>")
