import subprocess
r = subprocess.run(['git','fetch','net-kotobase','main'],capture_output=True,text=True,timeout=120)
print('fetch rc',r.returncode, r.stderr[-200:])
r2 = subprocess.run(['git','merge-base','--is-ancestor','net-kotobase/main','HEAD'],capture_output=True,text=True)
print('ancestor rc', r2.returncode)
r3 = subprocess.run(['git','push','net-kotobase','HEAD:main'],capture_output=True,text=True,timeout=180)
print('push rc',r3.returncode)
print(r3.stdout[-800:]); print(r3.stderr[-800:])
