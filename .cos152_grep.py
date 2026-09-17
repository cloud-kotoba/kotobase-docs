import re

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()

pats = {
    "RUNIDS": re.compile(r"run5[5-9][0-9]|run6[0-9][0-9]"),
    "RANK_NEXT": re.compile(r"rank 第2[4-9][0-9]回"),
    "BENCH_2026_09_09_10": re.compile(r"bench 2026-09-10"),
    "FALSIFY_2026_09_10": re.compile(r"falsify 2026-09-10"),
    "COSIENT_2026_09_10": re.compile(r"cosientist 2026-09-10"),
}

for name, pat in pats.items():
    hits = []
    for i, ln in enumerate(lines):
        if pat.search(ln):
            hits.append(i + 1)
    print(name, "hits lines:", hits[:20], "count:", len(hits))

# Print tail lines 2740-2759 already seen. Now find the iteration log section header
for i, ln in enumerate(lines):
    if ln.strip().startswith("#") and ("Iteration" in ln or "iteration" in ln or "反復" in ln):
        print("SECTION", i + 1, ln[:120])
