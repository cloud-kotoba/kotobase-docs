import re

text = open("query-cosientist.md", encoding="utf-8").read()

# Extract the run103 sentence(s)
idx = text.find("run103")
snippet = text[max(0, idx - 300): idx + 900]
with open("kz3_run103_ctx_out.txt", "w", encoding="utf-8") as f:
    f.write(snippet)

# Count occurrences of run103 to see which bots already used it
occs = [m.start() for m in re.finditer(r"run103", text)]
with open("kz3_run103_math.txt", "w", encoding="utf-8") as f:
    f.write("run103 occurrence count: %d\n" % len(occs))
    f.write("bench numbered runs found: %s\n" % sorted(
        int(n) for n in re.findall(r"bench 第(\d+)回", text))[-6:])
print("ok")
