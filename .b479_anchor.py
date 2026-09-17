import subprocess
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r=subprocess.run(["git","show","HEAD:query-cosientist.md"],cwd=p,capture_output=True,text=True,encoding="utf-8").stdout
lines=r.split("\n")
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        print("KZ3 row idx",i)
        print("tail:",l[-450:])
        print("run478 in row?", "run478" in l)
        print("ends with pipe?", l.rstrip().endswith("|"))
    if l.startswith("## Iteration log"):
        print("ITER header idx",i)
        print("next line:",lines[i+1][:120])
        break