# -*- coding: utf-8 -*-
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()
print("TOTALLINES:", len(lines))
ln = lines[403]  # K-Z3 cell tail
print("run477 in L404:", "run477A" in ln, "| run474 in L404:", "run474A" in ln)
print("TAIL200:", ln[-200:])
