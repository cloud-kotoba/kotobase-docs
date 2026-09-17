#!/usr/bin/env python3
# patch the qstrip fn in .b419_insert.py to also strip combining marks U+0300-U+036F
fn = ".b419_insert.py"
s = open(fn, encoding="utf-8").read()
old = (
    'def qstrip(s):\n'
    '    return s.replace(\"\\u200b\",\"\").replace(\"\\u200c\",\"\").replace(\"\\u200d\",\"\").replace(\"\\ufeff\",\"\")\n'
)
new = (
    'def qstrip(s):\n'
    '    return "".join(c for c in s if not ("\\u200b" == c or "\\u200c" == c or "\\u200d" == c or "\\ufeff" == c or "\\u0300" <= c <= "\\u036f"))\n'
)
assert s.count(old) == 1, ("old not found once", s.count(old"))
s = s.replace(old, new)
open(fn, "w", encoding="utf-8").write(s)
print("QFIX ok")