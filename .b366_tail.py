p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p) as f:
    lines=f.readlines()
l279=lines[278]  # 0-indexed line 279
tail=l279[-1500:]
print("LEN279=",len(l279))
print("=== TAIL 1500 ===")
print(tail)