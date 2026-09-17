import os
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
for f in sorted(os.listdir(d)):
    if f.endswith(".py"):
        head = open(os.path.join(d, f), encoding="utf-8", errors="replace").read(400).replace("\n", " | ")
        print(f, "::", head[:260])
        print()
