import io
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8") as f:
    lines = f.read().split("\n")
full = "\n".join(lines)
# evidence inside row cell?
l279 = lines[278]
print("L279 tail has run317:", "run317A\u2013C" in l279)
print("L279 tail:", l279[-160:])
# find iter header and check entry below
hdr = l279.find
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        print("iter hdr at L", i+1)
        print("next line:", lines[i+1][:80])
        break
# counts
print("run317 occurrences in L279:", l279.count("run317"))
print("run318 occurrences:", full.count("run318"))
# make sure stray line gone: line before iter header should be fold line
print("line before hdr tail:", lines[i-1][-70:])