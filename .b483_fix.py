# -*- coding: utf-8 -*-
import io
DOC="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(DOC,"r",encoding="utf-8") as f:
    t=f.read()
# replace U+2011 (non-breaking hyphen) leading my iter entry with normal '-'
t=t.replace("\u2011 2026-09-08: bench 第210回。16:54 JST tick",
            "- 2026-09-08: bench 第210回。16:54 JST tick")
with io.open(DOC,"w",encoding="utf-8") as f:
    f.write(t)
print("FIX_OK nbsp_hyphen_left=%d" % t.count("\u2011"))