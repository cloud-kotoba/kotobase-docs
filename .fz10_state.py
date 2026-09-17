import subprocess, re, json

out = {}
# git log last 30 oneline
lg = subprocess.run(["git","log","--oneline","-30"], capture_output=True, text=True)
out["gitlog"] = lg.stdout

# scan for run IDs in recent commit subjects
ids = re.findall(r"run(\d+)", lg.stdout)
out["run_ids_seen"] = sorted(set(int(x) for x in ids))

p = "query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()

out["nlines"] = len(lines)

# K-Z3 row: find line starting with "| K-Z3 |"
kz3_idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        kz3_idx = i
        break
out["kz3_line_1based"] = (kz3_idx + 1) if kz3_idx is not None else None
if kz3_idx is not None:
    row = lines[kz3_idx]
    out["kz3_len"] = len(row)
    out["kz3_tail_600"] = row[-600:]

# iteration log position
ilog_idx = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        ilog_idx = i
        break
out["ilog_line_1based"] = (ilog_idx + 1) if ilog_idx is not None else None
if ilog_idx is not None:
    out["ilog_next5"] = [l[:260] for l in lines[ilog_idx+1: ilog_idx+6]]

# status column of open hypotheses rows
for h in ["K-Q1","K-S1","K-S2","K-Z2","K-Z3"]:
    for l in lines:
        if l.startswith("| %s |" % h):
            out["row_%s_head" % h] = l[:300]
            break

with open(".fz10_state_out.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("done")
