import subprocess
r = subprocess.run(["git", "log", "--oneline", "-2"], capture_output=True, text=True)
s = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
p = subprocess.run(["git", "push"], capture_output=True, text=True)
with open("bench47_git_out.txt", "w") as f:
    f.write("LOG:\n" + r.stdout + r.stderr + "\nSTATUS:\n" + s.stdout +
            "\nPUSH rc=" + str(p.returncode) + "\n" + p.stdout + p.stderr)
