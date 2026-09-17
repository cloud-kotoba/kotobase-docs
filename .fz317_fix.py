import io

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(PATH, encoding="utf-8") as f:
    lines = f.read().split("\n")

# idx 357 (L358) is my stray evidence line
assert lines[357].startswith(" falsify 2026-09-07 (第146回"), f"unexpected L358: {lines[357][:60]}"
EV = lines[357].strip()
# remove stray line
del lines[357]

# append EV to end of the K-Z3 row (idx 278 = L279)
assert lines[278].startswith("| K-Z3 |"), f"L279 not row: {lines[278][:40]}"
lines[278] = lines[278].rstrip() + " " + EV

# sanity: Iteration log header and my iter-log entry
assert "## Iteration log" in lines
assert "- 2026-09-07: falsify 第146回" in "\n".join(lines), "iter-log entry missing"
assert lines[357] == "## Iteration log" or "## Iteration log" in lines, "iter header check"

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("FIXED: removed stray line, moved EV into L279")
print("EV len:", len(EV))