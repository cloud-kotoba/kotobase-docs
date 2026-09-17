import io
data = io.open("query-cosientist.md", encoding="utf-8").read()
lines = data.split("\n")
l279 = lines[278]
print("L279LEN=%d" % len(l279))
print("TAILSTART: " + l279[-1600:].replace("\r", "\\r"))
print("===HEADERSCAN===")
hdr_idx = None
for i in range(len(lines)):
    if lines[i].strip() == "## Iteration log":
        hdr_idx = i
        break
print("HDRIDX=" + repr(hdr_idx))
if hdr_idx is not None:
    hdr = lines[hdr_idx]
    print("HDRLINE=" + repr(hdr))
    stop = hdr_idx + 1 + 4
    if stop > len(lines):
        stop = len(lines)
    for j in range(hdr_idx+1, stop):
        s = lines[j]
        ls = len(s)
        ln = j + 1
        print("LINE" + str(ln) + " LEN=" + str(ls))
        print("HEAD=" + repr(s[:70]))
        print("TAILPG=" + repr(s[-120:])))))