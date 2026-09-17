import subprocess

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
out = open("kz3_run105_push3_out.txt", "w", encoding="utf-8")

def run(*args, **kw):
    r = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True, **kw)
    out.write(f"$ git {' '.join(args)}\nrc={r.returncode}\n{r.stdout}{r.stderr}\n---\n")
    return r

r = run("pull", "--rebase", "net-kotobase", "main")
if r.returncode == 0:
    run("push", "net-kotobase", "HEAD:main")
run("log", "--oneline", "-3")
out.close()
print("ok")
