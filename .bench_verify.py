import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(p, encoding="utf-8").read().split("\n")
keys = ["run504", "run505", "run503", "22hr", "21hr", "21時台", "第221", "第224", "run506"]
found = {}
for i, ln in enumerate(lines, 1):
    for k in keys:
        if k in ln:
            found.setdefault(k, []).append(i)
for k in keys:
    print("KEY", k, "->", found.get(k))
print("LAST_LINE", len(lines))
# print iter-log section full tail: lines 2580..2606
print("=== 2575..2606 ===")
for i in range(2575, min(2607, len(lines)+1)):
    print(i, "|", lines[i-1][:200])