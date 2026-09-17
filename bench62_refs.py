import subprocess
r = subprocess.run(['git','ls-remote','net-kotobase'],capture_output=True,text=True,timeout=120)
print(r.stdout)
print(r.stderr[-300:])
r2 = subprocess.run(['git','branch','--show-current'],capture_output=True,text=True)
print('local branch:', r2.stdout)
