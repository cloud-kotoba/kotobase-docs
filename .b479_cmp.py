import subprocess,re
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
# HEAD version
h=subprocess.run(["git","show","HEAD:query-cosientist.md"],cwd=p,capture_output=True,text=True,encoding="utf-8").stdout
hl=h.split("\n")
for i,l in enumerate(hl):
    if l.startswith("| K-Z3 | worker |"):
        print("HEAD row idx",i)
        print("HEAD row tail:",l[-400:])
        print("HEAD run478?", "run478" in l, " run477?", "run477" in l, " run476?", "run476" in l)
        break
# working
w=open(p+"/query-cosientist.md",encoding="utf-8").read()
for i,l in enumerate(w.split("\n")):
    if l.startswith("| K-Z3 | worker |"):
        print("WORK row idx",i)
        print("WORK run477?", "run477" in l, " run478?", "run478" in l, " run476?", "run476" in l)
        break
print("HEAD file lines unstaged tracked vs work:")
print("HEAD count477", hl.count("run477"))