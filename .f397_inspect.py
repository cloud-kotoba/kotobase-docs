import re,sys
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(fn,encoding="utf-8").read().split("\n")
# L279 is index 278
idx=278
l=lines[idx]
print("LEN279",len(l))
print("PREFIX",repr(l[:80]))
print("SUFFIX",repr(l[-120:]))
# find iter log header
for i,ln in enumerate(lines):
    if ln.strip().startswith("## Iteration log"):
        print("ITERLOG_HEAD",i+1)
        break
# count occurrences of falsify 第 and highest
fs=[int(m) for m in re.findall(r"falsify 第(\d+)回", open(fn,encoding="utf-8").read())]
print("MAX_FALSIFY", max(fs) if fs else None)