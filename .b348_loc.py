#!/usr/bin/env python3
import re
src=open("query-cosientist.md",encoding="utf-8").read()
lines=src.split("\n")
print("total lines:", len(lines))
# find K-Z3 hypothesis evidence line
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        print(f"--- K-Z3 evidence line at index {i} (1-based {i+1}) length {len(l)} ---")
        print("LAST 900 chars:")
        print(l[-900:])
        break
# find iterlog header
for i,l in enumerate(lines):
    if "Iteration log" in l or "iteration log" in l or "## " in l and "log" in l.lower():
        print(f"\n--- iterlog candidate at index {i} (1-based {i+1}): {l[:120]} ---")
        print(f"    line {i+2}: {lines[i+1][:150]}")
        print(f"    line {i+3}: {lines[i+2][:150]}")