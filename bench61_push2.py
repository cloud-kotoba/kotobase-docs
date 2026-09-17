import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(*a):
    r = subprocess.run(a, cwd=repo, capture_output=True, text=True)
    print("$", " ".join(a), "->", r.returncode)
    print(r.stdout[-1200:])
    if r.stderr.strip():
        print("ERR:", r.stderr[-600:])
    return r.returncode

# rebase onto latest net-kotobase/main, then push
run("git", "fetch", "net-kotobase", "main")
run("git", "rebase", "net-kotobase/main")
rc = run("git", "push", "net-kotobase", "HEAD:main")
print("PUSH_RC", rc)
run("git", "log", "--oneline", "-3")
