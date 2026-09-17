import io
fn = "query-cosientist.md"
s = open(fn, encoding="utf-8").read()
lines = s.split("\n")
# find iteration log entries (falsify 第9x回) and the K-Z3 hypothesis row
idxs = [i for i,l in enumerate(lines) if "falsify 第92回" in l]
print("f97 line:", [i+1 for i in idxs])
idx3 = [i for i,l in enumerate(lines) if "| K-Z3 | worker |" in l]
print("K-Z3 hyp row lines:", [i+1 for i in idx3])
# show a few lines around the falsify 92 entry
for i in idxs:
    for j in range(max(0,i-1), min(len(lines), i+3)):
        print(j+1, lines[j][:90])