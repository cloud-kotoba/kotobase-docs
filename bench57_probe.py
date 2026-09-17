import subprocess, sys
r = subprocess.run(['git','log','--oneline','-3'], capture_output=True, text=True, cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
sys.stdout.write("STDOUT:"+r.stdout+"\nSTDERR:"+r.stderr+"\nRC:"+str(r.returncode))
