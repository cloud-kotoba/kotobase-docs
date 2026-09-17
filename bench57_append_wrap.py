import subprocess
r=subprocess.run(['python3','/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench57_append.py'],capture_output=True,text=True)
open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench57_append_err.txt','w').write("RC:"+str(r.returncode)+"\nOUT:"+r.stdout+"\nERR:"+r.stderr)
