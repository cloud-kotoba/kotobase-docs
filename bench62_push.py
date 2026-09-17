import subprocess
r = subprocess.run(['git','push','net-kotobase','HEAD:net-kotobase'],capture_output=True,text=True,timeout=180)
print('rc',r.returncode)
print(r.stdout[-1500:])
print(r.stderr[-1500:])
