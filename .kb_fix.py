import sys
p = "query-cosientist.md"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()
fixed = False
for i, l in enumerate(lines):
    if l.startswith("- - 2026-09-08: falsify 第226回"):
        lines[i] = l[2:]  # strip leading "- "
        fixed = True
if not fixed:
    sys.stdout.write("NOT FOUND\n")
    sys.exit(3)
with open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
sys.stdout.write("FIXED\n")