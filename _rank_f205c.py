p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
line = open(p, encoding="utf-8").read().splitlines()[206]
# find run205 context within the K-Z3 evidence cell
idx = line.find("run205")
while idx != -1 and idx < len(line):
    print("...", line[max(0,idx-200):idx+1200])
    break
