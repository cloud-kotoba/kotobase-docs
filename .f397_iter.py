import re
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(fn,encoding="utf-8").read().split("\n")
for i,ln in enumerate(lines):
    if ln.strip().startswith("## Iteration log"):
        print("ITERLOG_HEAD line",i+1)
        print("next line:",repr(lines[i+1][:100]))
        print("next2:",repr(lines[i+2][:100]))
        break
# find where K-Z3 evidence row END marker would be: L279 is line 279 (index 278)
print("L279 is K-Z3 row len", len(lines[278]))