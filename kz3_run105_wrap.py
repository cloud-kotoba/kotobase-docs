import subprocess
r = subprocess.run(["python3", "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run105_calc.py"], capture_output=True, text=True)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run105_calc_out.txt", "w").write(r.stdout + r.stderr)
