#!/usr/bin/env python3
zws = set(["\u200b", "\u200c", "\u200d", "\ufeff"])
with open("query-cosientist.md", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        hits = [c for c in line if c in zws]
        if hits:
            pos = line.find(next((c for c in zws if c in line), ""))
            print("line", i, "col", pos, "chars", "".join(set(hits)), "ctx>", repr(line[max(0,pos-25):pos+10]))