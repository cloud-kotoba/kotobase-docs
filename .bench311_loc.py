#!/usr/bin/env python3
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
print("total_lines", len(lines))
# Find the K-Z3 row header and the evidence cell.
# Table row: "| K-Z3 | worker | ... | <evidence> |"
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 | worker |'):
        print("K-Z3 row starts at line", i+1, "len", len(ln))
        # print tail 600 chars
        print("TAIL:", ln[-600:])
        print("..idx", len(ln))