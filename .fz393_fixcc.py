#!/usr/bin/env python3
path = "query-cosientist.md"
s = open(path, encoding="utf-8").read()
old = "run393A\u2013C\u2013C"
new = "run393A\u2013C"
cnt = s.count(old)
print("occurrences:", cnt)
s = s.replace(old, new)
# fix the deduped text: "run393A–C 追加" should read "run393A–C 20時台 n 積み増し" context; verify
open(path, "w", encoding="utf-8").write(s)
# post-check
idx = s.find(new + " 追加")
print("after fix context:", repr(s[idx-70:idx+30]) if idx>0 else "-")
print("remaining CC:", s.count(old))