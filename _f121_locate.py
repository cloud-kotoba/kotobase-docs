import io

FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(FN, encoding="utf-8").read()

# locate the run265 cosientist evidence end (marker at end of that entry)
marker = "帯区分算入可否・status 判定は rank に委ねる (rank 専門)"
idx = data.rfind(marker)
print("marker idx:", idx)
if idx == -1:
    raise SystemExit("marker not found")

snip = data[idx:idx+80]
print("SNIP:", repr(snip))