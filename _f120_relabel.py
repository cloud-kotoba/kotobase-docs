import io

# Relabel my independent 23:31 measurement from run262 -> run263
# (run262 already used by bench 106 at 23:22; adopt run263 per run216/run224/run256 precedent)
src = "_f120_run262_out.txt"
out = "_f120_run263_out.txt"
lines = []
for line in io.open(src, encoding="utf-8"):
    lines.append(line.replace("run262", "run263"))
io.open(out, "w", encoding="utf-8").writelines(lines)
print("wrote", out, len(lines), "lines")
cnt = sum(1 for l in lines if l.startswith("run263"))
print("rulabeled run263 lines:", cnt)