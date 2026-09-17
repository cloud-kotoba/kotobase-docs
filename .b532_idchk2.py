import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    content = f.read()
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b532_idchk2.txt", "w", encoding="utf-8") as f:
    for rid in ("run612", "run613", "run614", "run615"):
        f.write(f"{rid}={content.count(rid)}\n")
print("ok")
