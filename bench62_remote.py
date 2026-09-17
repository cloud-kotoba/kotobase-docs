import subprocess
r = subprocess.run(['git','remote','-v'],capture_output=True,text=True)
print(r.stdout or r.stderr)
