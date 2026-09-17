import subprocess
r = subprocess.run(["git","push","net-kotobase","HEAD:main"], capture_output=True, text=True)
open("/tmp/rank56_push2.txt","w").write(f"RC={r.returncode}\n{r.stdout}\n{r.stderr}\n")
r2 = subprocess.run(["git","rev-parse","net-kotobase/main"], capture_output=True, text=True)
open("/tmp/rank56_push2.txt","a").write(f"remote_main_after={r2.stdout.strip()}\n")
