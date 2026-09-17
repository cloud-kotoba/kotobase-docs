import io, sys

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
out.append("total_lines=%d" % len(lines))

# find K-Z3 hypothesis rows (open hypotheses table) and the evidence tail line
kz3_rows = []
iter_header = None
for i, ln in enumerate(lines):
    if "| K-Z3 |" in ln and "worker |" in ln:
        kz3_rows.append(i+1)
    if ln.strip() == "## Iteration log":
        iter_header = i  # 0-indexed
    # not breaking

out.append("kz3_worker_rows=%s" % kz3_rows)
out.append("iter_header_line=%s" % (iter_header+1 if iter_header is not None else None))

# Does any line end with '|' ?
if kz3_rows:
    r = kz3_rows[0]-1
    ln = lines[r]
    out.append("kz3_row_len=%d" % len(ln))
    out.append("kz3_row_endswith_pipe=%s" % ln.rstrip().endswith("|"))
    out.append("kz3_row_last80=%r" % ln.rstrip()[-120:])
    out.append("kz3_row_runs=%d" % ln.count("run"))

# check run497 anywhere
cnt497 = 0
for ln in lines:
    cnt497 += ln.count("run497")
out.append("run497_count=%d" % cnt497)

# check run496
cnt496 = 0
for ln in lines:
    cnt496 += ln.count("run496")
out.append("run496_count=%d" % cnt496)

with io.open("/tmp/bench_probe497.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
