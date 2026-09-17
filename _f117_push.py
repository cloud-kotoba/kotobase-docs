import subprocess
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
# stage only the state file
subprocess.run(['git','add','query-cosientist.md'],cwd=D,check=True)
subprocess.run(['git','commit','-m','falsify 第117回: K-Z3 22時台 n 積み増し run256A-C cold 2/60 (~3.3%), control 分離成立 (散発ペア型)'],cwd=D,check=True)
r=subprocess.run(['git','push','net-kotobase','HEAD:main'],cwd=D,capture_output=True,text=True)
head=subprocess.run(['git','rev-parse','HEAD'],cwd=D,capture_output=True,text=True).stdout.strip()
with open('/tmp/f117_push.txt','w') as f:
    f.write("push rc=%d\n%s\n%s\nHEAD=%s\n" % (r.returncode, r.stdout[-1500:], r.stderr[-800:], head))
print("done")