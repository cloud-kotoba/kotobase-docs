import os
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
names=sorted(os.listdir(D))
scripts=[n for n in names if n.endswith(('.py','.sh','.mjs'))]
with open(D+'/bench57_ls.txt','w') as f:
    f.write("SCRIPTS:\n"+"\n".join(scripts)+"\n\nALL ("+str(len(names))+"):\n"+"\n".join(names))
