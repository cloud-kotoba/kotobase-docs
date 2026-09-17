import subprocess, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
def run(*args):
    r = subprocess.run(args, capture_output=True, text=True)
    return (r.returncode, r.stdout.strip(), r.stderr.strip())
cmds = [
    ["git", "add", "query-cosientist.md"],
    ["git", "commit", "-m",
     "rank 第56回: bench 第56回 (PR #614 merge 済独立確認, header 0→3 未達) を取り込み — "
     "残る切れ手は gateway deploy 実行 (cosientist) に収束, status 遷移なし, 順位変動なし, "
     "NEXT: K-Q1 gateway deploy 実行 (main 364b3355) + deploy 後 header 到達確認 0→30 (bench/falsify)"],
    ["git", "push", "net-kotobase", "main"],
]
with open("/tmp/rank56_commit.txt", "w") as f:
    for c in cmds:
        rc, out, err = run(*c)
        f.write(f"$ {' '.join(c)}\nRC={rc}\n{out}\n{err}\n---\n")
