import subprocess

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
out = open("kq1_commit_out.txt", "w", encoding="utf-8")

def run(*args):
    r = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True)
    out.write(f"$ git {' '.join(args)}\nrc={r.returncode}\n{r.stdout}{r.stderr}\n---\n")
    return r

# 追跡対象は query-cosientist.md のみ (作業ファイルは commit しない)
run("add", "query-cosientist.md")
r = run("commit", "-m",
        "bench 第36回: K-Q1 quiet-host local 測定 2 本 (graph-for p50 0.018ms で寄与せず, "
        "verify-session 1 hop p50 11.81ms — 1 重化の削減上限 ~12ms で退行主因ではない)")
if r.returncode == 0:
    run("pull", "--rebase", "net-kotobase", "main")
    run("push", "net-kotobase", "HEAD:main")
run("log", "net-kotobase/main", "--oneline", "-2")
out.close()
print("ok")
