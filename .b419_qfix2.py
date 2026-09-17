#!/usr/bin/env python3
# splice a combining-mark-stripping qstrip into .b419_insert.py
fn = ".b419_insert.py"
s = open(fn, encoding="utf-8").read()
start = s.index("def qstrip")
end = s.index("\n\n", start)
newblock = (
    "def qstrip(s):\n"
    "    return \"\".join(c for c in s if not (c in \"\\u200b\\u200c\\u200d\\ufeff\" or \"\\u0300\" <= c <= \"\\u036f\"))\n"
)
s = s[:start] + newblock + s[end:]
open(fn, "w", encoding="utf-8").write(s)
print("QFIX2 ok")