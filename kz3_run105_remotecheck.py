import subprocess

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
out = open("kz3_run105_remotecheck.txt", "w", encoding="utf-8")

def run(*args):
    r = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True)
    out.write(f"$ git {' '.join(args)}\nrc={r.returncode}\n{r.stdout}{r.stderr}\n---\n")

run("remote", "-v")
run("branch", "-vv")
run("config", "--get-regexp", r"branch\..*")
run("log", "--oneline", "-3")
out.close()
print("ok")
