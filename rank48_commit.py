import subprocess, datetime

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
lines = []
def run(*cmd):
    p = subprocess.run(list(cmd), cwd=cwd, capture_output=True, text=True)
    lines.append("$ " + " ".join(cmd))
    lines.append(p.stdout.strip())
    if p.stderr.strip():
        lines.append("STDERR: " + p.stderr.strip())
    lines.append("RC=%d" % p.returncode)
    lines.append("")
    return p

run("git", "add", "query-cosientist.md")
run("git", "commit", "-m",
    "rank 第48回: PR #3 merge+deploy 完了を取り込み (cosientist 第50回), K-Z3 13/14時台 evidence 追記反映, NEXT: K-Q1 deploy 後 header 計測")
run("git", "push")
run("git", "log", "--oneline", "-3")
run("git", "status", "--short", "query-cosientist.md")
with open(cwd + "/rank48_commit_out.txt", "w") as f:
    f.write("\n".join(lines))
