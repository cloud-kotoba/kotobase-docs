import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    lines = f.readlines()
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b532_idchk.txt", "w", encoding="utf-8") as f:
    for i, l in enumerate(lines, 1):
        for rid in ("run595", "run596", "run597", "run598", "run599", "run600"):
            if rid in l:
                pos = l.find(rid)
                f.write(f"L{i} {rid}: ...{l[max(0,pos-120):pos+180]}...\n")
print("ok")
