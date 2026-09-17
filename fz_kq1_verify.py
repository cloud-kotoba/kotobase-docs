#!/usr/bin/env python3
import subprocess
d = subprocess.run(["git", "diff", "query-cosientist.md"], capture_output=True, text=True).stdout
# show the added part only (lines starting with +)
for line in d.splitlines():
    if line.startswith("+") and not line.startswith("+++"):
        print("ADDED (len", len(line), "):")
        print(line[:400])
        print("...")
        print(line[-400:])
print("<<END>>")
