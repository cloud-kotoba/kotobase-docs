import io
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8") as f:
    lines = f.read().split("\n")
for i in [278, 356, 357, 358, 359]:
    ln = lines[i] if i < len(lines) else "<EOF>"
    print(f"=== idx {i} (L{i+1}) len={len(ln)} ===")
    print(f"  head: {ln[:70]}")
    print(f"  tail: {ln[-110:]}")
print("TLEN", len(lines))