#!/usr/bin/env python3
import sys
txt = open("query-cosientist.md").read().splitlines()
for i, line in enumerate(txt, 1):
    if line.startswith("| K-Q1 "):
        sys.stdout.write(line[800:2400])
        sys.stdout.write("\n<<END>>\n")
