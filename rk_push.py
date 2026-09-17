import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    p = subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()

rc, out, err = run(["add", "query-cosientist.md"])
print("add rc:", rc, err)
rc, out, err = run(["commit", "-m", "rank 第34回: K-Z3 深夜帯 23時台 run99A/100A/101A 取り込み — cold 単独クラスタ型 3 例連続で traffic 依存説は弱まる, status 遷移なし, NEXT K-Z3 0時台 n=20 x 3 + control"])
print("commit rc:", rc, out, err)
rc, out, err = run(["push", "net-kotobase", "HEAD:main"])
print("push rc:", rc, out, err)
rc, out, err = run(["log", "HEAD", "--oneline", "-2"])
print(out)
