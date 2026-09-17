import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(*args):
    return subprocess.run(["git"] + list(args), cwd=repo, capture_output=True, text=True)
r = run("add", "query-cosientist.md")
print("add:", r.returncode, r.stderr.strip())
r = run("commit", "-m",
        "bench 第50回: K-Z3 17時台 n 積み増し run156A–C (cold 1/60 ~1.7%, 17時台通算 6/120 ~5.0% 低位帯, "
        "control 静穏, search 局在 1s 超単発外れ値 1 件) evidence + iteration log 追記 — status 遷移なし")
print("commit:", r.returncode, r.stdout.strip(), r.stderr.strip())
r = run("push", "net-kotobase", "HEAD:main")
print("push:", r.returncode, r.stdout.strip(), r.stderr.strip())
r = run("log", "--oneline", "-1")
print("head:", r.stdout.strip())
