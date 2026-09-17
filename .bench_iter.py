import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(p, encoding="utf-8").read().split("\n")
# find all lines containing 'Iteration log' header variants
for i, ln in enumerate(lines, 1):
    if ln.strip().startswith("##") and "Iteration" in ln:
        print("HDR", i, repr(ln))
# find last N non-empty lines
nonempty = [(i+1, ln) for i, ln in enumerate(lines) if ln.strip()]
print("TOTAL_LINES", len(lines), "NONEMPTY", len(nonempty))
print("=== last 12 non-empty ===")
for i, ln in nonempty[-12:]:
    print(i, "|", ln[:300])