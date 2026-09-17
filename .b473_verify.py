#!/usr/bin/env python3
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(P, encoding="utf-8").read()
lines = data.split("\n")
out = []
# locate iter header and check entry order
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        out.append("ITER_HDR line=%d" % (i+1))
        out.append("NEXT1 %r" % lines[i+2][:80])
    if "run473" in l:
        out.append("RUN473 at line=%d start=%r" % (i+1, l[:70]))
# secret check
for kw in ["cookie", "Bearer ", "authorization", "token=", "api_key", "credential"]:
    if kw in data:
        out.append("SECRETLIKE %r" % kw)
out.append("TOTAL_LINES %d" % len(lines))
with open("/tmp/b473_verify.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print("ok")