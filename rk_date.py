import subprocess
p = subprocess.run(["date"], capture_output=True, text=True)
print(p.stdout.strip())
p2 = subprocess.run(["uptime"], capture_output=True, text=True)
print(p2.stdout.strip())
