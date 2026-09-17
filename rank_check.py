r = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank_out.txt","w")
import subprocess
p = subprocess.run(["date"], capture_output=True, text=True)
p2 = subprocess.run(["git","log","--oneline","-3"], capture_output=True, text=True,
                    cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
p3 = subprocess.run(["git","status","--short"], capture_output=True, text=True,
                    cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
r.write("DATE:\n"+p.stdout+p.stderr+"\nLOG:\n"+p2.stdout+p2.stderr+"\nSTATUS:\n"+p3.stdout[:500])
r.close()
