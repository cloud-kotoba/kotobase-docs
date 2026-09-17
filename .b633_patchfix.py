#!/usr/bin/env python3

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b633_edit.py"
with open(p) as f:
    src = f.read()
old = 'endswith(")")'
new = 'endswith("(rank 専門)。")'
assert src.count(old) == 1, "occurrence check"
with open(p, "w") as f:
    f.write(src.replace(old, new))
print("patched")
