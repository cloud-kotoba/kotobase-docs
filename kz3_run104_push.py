import subprocess

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r = subprocess.run(["git", "remote", "-v"], cwd=cwd, capture_output=True, text=True)
r2 = subprocess.run(["git", "push", "net-kotobase", "cosient-sync:main"],
                    cwd=cwd, capture_output=True, text=True)
with open("kz3_run104_push_out.txt", "w", encoding="utf-8") as f:
    f.write("remotes:\n%s\npush rc=%s\n%s\n%s\n" % (r.stdout, r2.returncode,
                                                    r2.stdout, r2.stderr))
print("ok")
