import subprocess

def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=".")
    with open("fz160_git.txt", "a") as f:
        f.write("$ " + " ".join(args) + "\n" + (r.stdout or "") + (r.stderr or "") + "\n")

open("fz160_git.txt", "w").close()
run(["git", "add", "query-cosientist.md"])
run(["git", "commit", "-m", "falsify 第58回: K-Z3 18時台 control 付き追加 n run160A-C (search cold 2/60, 18時台通算 3/120 ~2.5% 低位帯, p50 50-182ms 帯に復帰) — landing control 上振れで run158 型全体遅延窓が 18:01/18:35 の 2 窓で再出現 (部分 not-separated) evidence + iteration log 追記 — status 遷移なし"])
run(["git", "push", "net-kotobase", "HEAD:main"])
run(["git", "log", "--oneline", "-1"])
