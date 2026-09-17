import io
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(fn,encoding="utf-8").read().split("\n")
# find row line starting with "| K-Z3 |"
idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=i; break
if idx is None:
    print("K-Z3 row not found"); raise SystemExit
print("ROW_LINE=%d"%(idx+1))
print("ROW_LEN=%d"%len(lines[idx]))
print("TAIL_START=%d"%(len(lines[idx])-700))
print(lines[idx][-700:])