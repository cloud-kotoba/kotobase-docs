# -*- coding: utf-8 -*-
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()
for i in range(403, 0, -1):
    ln = lines[i]
    if "run474" in ln or "run475" in ln or "run476" in ln or "run473A" in ln:
        print(i+1, "hit_run473-476")
    # print candidate tail lines near the end of the K-Z3 cell
# find the last line index containing run473/474 to know cell end
for i in range(390, 405):
    tag = []
    for r in ["run468","run469","run470","run471","run472","run473","run474","run475","run476"]:
        if r in lines[i]:
            tag.append(r)
    print(i+1, tag, "LEN", len(lines[i]))
