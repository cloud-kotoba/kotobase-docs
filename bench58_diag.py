import subprocess, re

r = subprocess.run(["git", "pull", "--ff-only"], capture_output=True, text=True)
content = open("query-cosientist.md", encoding="utf-8").read()
seg = content.split("bench 2026-09-05 (第58回")[1].split("status 判定は rank に委ねる (rank 専門)。")[0]
with open("bench58_diag_out.txt", "w") as f:
    f.write("pull: %s\n" % (r.stdout.strip() or r.stderr.strip()))
    f.write("entry run171 refs: %d / residual run170 refs (excluding the explanation): %d\n" % (
        len(re.findall(r"run171", seg)),
        len(re.findall(r"run170", seg.replace("※ run170 は cosientist", "X")))))
    f.write("HEAD: %s\n" % subprocess.run(["git", "log", "-1", "--format=%h %s"], capture_output=True, text=True).stdout.strip())
