#!/usr/bin/env python3
import re
path = "query-cosientist.md"
s = open(path, encoding="utf-8").read()
lines = s.split("\n")
print("iterlog header count:", sum(1 for l in lines if l.strip()=="## Iteration log"))
print("K-Z3 row count:", sum(1 for l in lines if l.startswith("| K-Z3 |")))
print("run393 total mentions:", s.count("run393"))
print("run393A-C evidenced runs:", s.count("run393A"), s.count("run393B"), s.count("run393C"))
# zero-width / control chars
bad = re.findall(r"[\u200b\u200c\u200d\ufeff]", s)
print("zero-width chars:", len(bad))
# secret scan (redact-check)
sec = re.findall(r"(?i)(token|cookie|credential|secret\s*[:=]|bearer|passw)", s)
print("secret-ish mentions (in evidence tail 5000):", len(re.findall(r"(?i)(bearer|api[_-]?key|cookie)", s[-6000:])))
# iter-log newest first check
hdr = next(i for i,l in enumerate(lines) if l.strip()=="## Iteration log")
print("entry after header:", lines[hdr+1][:50])
print("L279 starts with:", lines[278][:12])
print("L279 run393 evidence present:", "run393A" in lines[278])