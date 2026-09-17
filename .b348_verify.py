#!/usr/bin/env python3
src=open("query-cosientist.md",encoding="utf-8").read()
lines=src.split("\n")
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        print("=== K-Z3 last 500 chars ===")
        print(l[-500:])
        break
print()
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        print("=== iterlog top (after header) ===")
        print(repr(l))
        for j in range(i+1,i+4):
            print(repr(lines[j][:200]))
        break