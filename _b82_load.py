import subprocess, os
p = subprocess.run(['uptime'], capture_output=True, text=True)
print(p.stdout.strip() or p.stderr.strip())
print('load1', os.getloadavg())
