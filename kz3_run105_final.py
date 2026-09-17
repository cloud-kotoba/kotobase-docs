import subprocess

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
out = open("kz3_run105_final.txt", "w", encoding="utf-8")

def run(*args):
    r = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True)
    out.write(f"$ git {' '.join(args)}\nrc={r.returncode}\n{r.stdout}{r.stderr}\n---\n")
    return r

run("fetch", "net-kotobase", "main")
run("rev-parse", "HEAD", "net-kotobase/main")
run("log", "net-kotobase/main", "--oneline", "-1")
# grep evidence line in the fetched file
run("grep", "-c", "run105A", "net-kotobase/main:query-cosientist.md")
out.close()
print("ok")
