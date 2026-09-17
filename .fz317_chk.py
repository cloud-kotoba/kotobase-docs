import io
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8") as f:
    lines = f.read().split("\n")
ln = lines[278]  # 0-based index 278 = line 279
idx = 0
while True:
    j = ln.find("run317", idx)
    if j < 0:
        break
    print(f"line279 run317 ctx: ...{ln[max(0,j-60):j+15]}...")
    idx = j + 1
for i in [357, 358, 359]:
    print(f"L{i+1} start: {lines[i][:60] if i < len(lines) else 'EOF'}")