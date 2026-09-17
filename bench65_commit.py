import subprocess

def run(*args):
    r = subprocess.run(args, capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", timeout=180)
    return r.returncode, (r.stdout + r.stderr).strip()

rc1, out1 = run("git", "add", "query-cosientist.md")
rc2, out2 = run("git", "commit", "-m",
    "docs: bench 第65回 evidence — K-Q1 transact 401 診断 (authn chain 200/201 で query 200, transact のみ 401 即断 = endpoint 固有) + K-Z3 4時台 run182A-C (cold 2/60 低位, control 静穏) + iteration log")
rc3, out3 = run("git", "push", "net-kotobase", "HEAD:net-kotobase/main")
rc4, out4 = run("git", "log", "--oneline", "-1")
with open("/tmp/bench65_git.txt", "w") as f:
    f.write(f"add rc={rc1} {out1}\ncommit rc={rc2} {out2}\npush rc={rc3} {out3}\nhead: {out4}\n")
print("rc", rc1, rc2, rc3, rc4)
