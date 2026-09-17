path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(path).read().splitlines()
keys = ["run244", "run245", "第111回", "第98回", "bench 第98回"]
for i, ln in enumerate(lines, 1):
    if "run244" in ln or "run245" in ln or "第98回" in ln and "bench" in ln:
        print(f"{i} ({len(ln)}ch): {ln[:120]}")