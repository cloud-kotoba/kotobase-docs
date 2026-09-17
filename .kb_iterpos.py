import sys
p = "query-cosientist.md"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()
out = []
for i, l in enumerate(lines):
    if l.startswith("## Iteration log"):
        out.append("iterlog at line %d" % (i + 1))
        out.append("NEXT1: %r" % lines[i + 1][:160])
        out.append("NEXT2: %r" % lines[i + 2][:160])
        break

# count falsify iteration numbers in iter log region
import re
nums = []
for l in lines:
    m = re.search(r"falsify 第(\d+)回", l)
    if m:
        nums.append(int(m.group(1)))
if nums:
    out.append("falsify max iter = %d (count %d)" % (max(nums), len(nums)))
sys.stdout.write("\n".join(out) + "\n")