#!/usr/bin/env python3
import io
PATH="query-cosientist.md"
s=io.open(PATH,encoding="utf-8").read()
n=s.count("同渫定法")
print("occurrences before:", n)
if n>0:
    s=s.replace("同渫定法","同測定法")
io.open(PATH,"w",encoding="utf-8").write(s)
print("replacements applied; after:", s.count("同渫定法"))