import subprocess, sys
out = subprocess.run(['python3','/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench57_probe.py'], capture_output=True, text=True)
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench57_probe_out.txt','w') as f:
    f.write(out.stdout + "\nERR:" + out.stderr + "\nRC:" + str(out.returncode))
