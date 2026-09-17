#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
f=io.open(p,encoding="utf-8")
lines=f.readlines(); f.close()
# find K-Z3 row
idx=None
for i,ln in enumerate(lines):
	if ln.startswith("| K-Z3 |"):
		idx=i; break
print("K-Z3 row line# =", idx+1)
if idx is not None:
	txt=lines[idx]
	print("row_len_chars=",len(txt))
	# tail 400 chars
	tail=txt[-400:]
	print("---TAIL_START---")
	print(tail)
	print("---TAIL_END---")
	# detect trailing pattern
	import re
	# last 60 visible chars after rstrip
	rs=txt.rstrip("\n")
	print("last80_after_rstrip=", rs[-80:])
# iter log header
for i,ln in enumerate(lines):
	if "## Iteration log" in ln:
		print("iterlog_header_line=",i+1)
		# print next 3 lines raw
		for j in range(i,i+4):
			print("C%03d|%r"%(j+1,lines[j] if j<len(lines) else"<EOF>"))
		break