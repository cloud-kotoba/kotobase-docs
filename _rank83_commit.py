import subprocess
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
cmds = [
    ["git", "-C", p, "add", "query-cosientist.md"],
    ["git", "-C", p, "commit", "-m", "rank 第83回: K-Q1 切れ手(i) scope 照合反証 (cosient 82続) + falsify 83/bench 82 run207 取り込み, K-Q1 切れ手 (ii) へ収束 + NEXT"],
    ["git", "-C", p, "fetch", "net-kotobase"],
    ["git", "-C", p, "rev-parse", "HEAD", "net-kotobase/main"],
    ["git", "-C", p, "push", "net-kotobase", "HEAD:main"],
]
out = []
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True)
    out.append(f"RC {r.returncode} :: {c[-1]}\nOUT {r.stdout[-800:]}\nERR {r.stderr[-800:]}")
with open("/tmp/rank83_commit.txt", "w") as f:
    f.write("\n".join(out))
