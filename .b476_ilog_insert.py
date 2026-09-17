import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
entry_path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b476_ilog_entry.txt"

with io.open(entry_path, "r", encoding="utf-8") as f:
    entry = f.read().strip()

with io.open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        idx = i
        break
if idx is None:
    raise SystemExit("header not found")

lines.insert(idx + 1, entry + "\n")

with io.open(path, "w", encoding="utf-8") as f:
    f.write("".join(lines))
print("OK idx=%d" % idx)