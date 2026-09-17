import subprocess
d='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
r=subprocess.run(['git','fetch','net-kotobase'],cwd=d,capture_output=True,text=True)
r2=subprocess.run(['git','rev-parse','HEAD','net-kotobase/main'],cwd=d,capture_output=True,text=True)
open('/tmp/fz127_pushverify.txt','w').write(r2.stdout+"\n"+r2.stderr)
