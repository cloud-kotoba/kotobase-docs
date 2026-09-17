#!/usr/bin/env python3
import unicodedata
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(path, encoding='utf-8').read()
lines = data.split('\n')
print("total_lines=%d" % len(lines))

# 1) combining-char scan (0x0300-0x036F) within the two inserted regions
bad = []
for ln,(idx,marker) in enumerate([("L279_ev","第241回, K-Z3"),("ilog","falsify 第241回")],1):
    pass
for idx in (278, 413):
    seg = lines[idx]
    for pos,ch in enumerate(seg):
        if 0x0300 <= ord(ch) <= 0x036F:
            bad.append((idx,pos,hex(ord(ch))))
print("combining_hits=%s" % (bad[:10] if bad else "none"))

# 2) K-Z3 row still single '| K-Z3 |' and ends with run543 evidence
print("L279_count_kz3rows=", sum(1 for l in lines if l.startswith('| K-Z3 |')))
print("L279_ends_with_run543_status=", lines[278][-40:])
print("L279_contains_run543=", "run543" in lines[278])

# 3) iter log top ordering
print("header_at=", lines[412][:20])
print("ilog_line1=", lines[413][:60])
print("rank240_line2=", lines[414][:40])

# 4) occurrences
print("run543_occurrences=", data.count('run543'))
print("falsify_第241回_occurrences=", data.count('第241回'))