import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(*a):
    r = subprocess.run(a, cwd=repo, capture_output=True, text=True)
    print("$", " ".join(a), "->", r.returncode)
    print(r.stdout[-1500:])
    if r.stderr.strip():
        print("ERR:", r.stderr[-800:])
    return r.returncode

run("git", "add", "query-cosientist.md", "bench61_run175.sh", "bench61_run175_out.txt")
run("git", "commit", "-m",
    "bench 第61回: K-Z3 23時台 n 積み増し run176A-C (cold 7/60, control 分離成立, 即消失型)")
rc = run("git", "pull", "--rebase", "origin", "main")
rc2 = run("git", "push", "origin", "HEAD:main")
print("PUSH_RC", rc2)
