import subprocess, sys

def run(args):
    r = subprocess.run(args, capture_output=True, text=True,
                       cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    return (r.returncode, r.stdout.strip(), r.stderr.strip())

rc, out, err = run(["git", "rev-parse", "HEAD"])
print("HEAD", rc, out, err)
rc, out, err = run(["git", "rev-parse", "net-kotobase/main"])
print("remote_main", rc, out, err)
rc, out, err = run(["git", "add", "query-cosientist.md"])
print("add", rc, out, err)
rc, out, err = run(["git", "commit", "-m",
    "rank 第49回: falsify 第53回 (K-Z3 16時台 run154A–C cold 9/60) + bench 第49回 (PR #3 merge済みだが production header 不在 6/6, transact 401 継続) を取り込み — status 遷移なし, rank ブロック第49回版へ差替え (順位変動なし K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2), NEXT: K-Q1 deploy 整合切分け (cosientist)"])
print("commit", rc, out, err)
