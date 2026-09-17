FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(FN, encoding="utf-8").read().split("\n")

# find the bench 第107回 run264 line (most recent 23時台 evidence line)
anchor = "第107回, K-Z3 23時台 n 積み増し run264A–C"
idx = None
for i, ln in enumerate(lines):
    if anchor in ln:
        idx = i
        break
print("anchor line idx:", idx)
if idx is None:
    raise SystemExit("anchor not found")

print("TARGET PREV line:", lines[idx][:60])
print("NEXT line:", lines[idx+1][:60] if idx+1 < len(lines) else "<EOF>")