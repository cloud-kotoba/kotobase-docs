import subprocess

def run(*args):
    return subprocess.run(args, capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")

r = run("git", "add", "query-cosientist.md")
print("add rc", r.returncode, r.stderr.strip())
r = run("git", "commit", "-m",
        "rank 第84回: falsify 84 run209 / bench 83 run210 (13時台帯初 6/60) 取り込み, K-Z3 帯別分布更新, 順位変動なし + NEXT K-Z3 13時台 n 積み増し")
print("commit rc", r.returncode, r.stdout.strip(), r.stderr.strip())
r = run("git", "push", "net-kotobase", "HEAD:main")
print("push rc", r.returncode, r.stdout.strip(), r.stderr.strip())
r = run("git", "rev-parse", "HEAD", "net-kotobase/main")
print(r.stdout)
