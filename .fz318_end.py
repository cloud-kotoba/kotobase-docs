p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
print("K-Z3 hypothesis row line index 278 (0-based), LEN", len(lines[278]))
# Show the last 800 chars of cell-end (line 357 0-based = index 356) and first 60 of iterlog
print("=== last 900 chars of index 356 ===")
print(lines[356][-900:])
print("=== index 357 ===")
print(repr(lines[357][:30]))
# Check how bench 132 run318 evidence appears: search iterlog benches
for i in range(358, 360):
    print("IL", i, repr(lines[i][:120]))