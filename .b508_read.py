# -*- coding: utf-8 -*-
import io, time
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = None
for attempt in range(15):
    try:
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()
        break
    except FileNotFoundError:
        time.sleep(0.8)
if txt is None:
    print("READ_FAILED_AFTER_RETRIES")
    raise SystemExit(1)
lines = txt.split("\n")
print("TOTAL_LINES", len(lines))
# iter log head
for i, ln in enumerate(lines, 1):
    if ln.startswith("## Iteration log"):
        print("ITERLOG_HEADER_LINE", i)
        for j in range(i, min(len(lines), i + 8)):
            s = lines[j].strip()
            if s.startswith("- "):
                print("LOGENTRY", j + 1, "|", s[:230])
        break
# run507/508 mentions in iter log area + evidence tail location
import re
print("run507_count", len(re.findall("run507", txt)))
print("run508_count", len(re.findall("run508", txt)))
# find the K-Z3 evidence row (the row that has K-Z3 and many run mentions)
for i, ln in enumerate(lines, 1):
    if ln.startswith("| K-Z3 "):
        print("KZ3_ROW", i, "|", ln[:120])
        break