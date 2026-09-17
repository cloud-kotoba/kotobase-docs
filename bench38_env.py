import subprocess, sys
with open("bench38_env_out.txt", "w") as f:
    r = subprocess.run(["date"], capture_output=True, text=True)
    f.write("DATE: " + r.stdout + r.stderr + "\n")
    r2 = subprocess.run(["sysctl", "-n", "vm.loadavg"], capture_output=True, text=True)
    f.write("LOADAVG: " + r2.stdout + r2.stderr + "\n")
    r3 = subprocess.run(["git", "log", "--oneline", "-3"], capture_output=True, text=True, cwd=".")
    f.write("GIT: " + r3.stdout + r3.stderr + "\n")
print("done")
