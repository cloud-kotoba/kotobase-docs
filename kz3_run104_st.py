import subprocess

p = subprocess.run(["git", "status", "--porcelain"],
                   capture_output=True, text=True,
                   cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
with open("kz3_run104_st_out.txt", "w", encoding="utf-8") as f:
    f.write("rc=%s\nstdout:\n%s\nstderr:\n%s\n" % (p.returncode, p.stdout, p.stderr))
print("ok")
