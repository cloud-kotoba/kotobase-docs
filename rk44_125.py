p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.split("\n")
# Show the run125 segment within line 175 (K-Z3 row)
i = lines[174].find("run125")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_125_out.txt","w").write(lines[174][max(0,i-1500):i+2000])
print("ok")
