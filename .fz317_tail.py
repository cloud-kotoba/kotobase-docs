import io
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8") as f:
    lines = f.read().split("\n")
for i in range(353, 361):
    if i < len(lines):
        print(f"{i+1}: [{lines[i][:150]}]")
print("---TLEN---", len(lines))