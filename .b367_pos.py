import os
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
for fn in [".b367_367A.txt", ".b367_367C.txt"]:
    rows = []
    for l in open(os.path.join(base,fn)):
        l = l.strip()
        if not l: continue
        rows.append(l.split())
    cold = []
    for i,(c,t) in enumerate(rows):
        if float(t) >= 0.5:
            cold.append((i+1,float(t)))
    print(fn, cold)