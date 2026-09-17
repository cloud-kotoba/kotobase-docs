import subprocess, sys
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
cmds = [
 ["git", "-C", p, "add", "query-cosientist.md"],
 ["git", "-C", p, "commit", "-m", "rank 第82回: K-Z3 10時台 8/240 + 11時台 4/60 取り込み, K-Q1 切れ手再収束 (parity 反証) を rank 更新 + NEXT"],
 ["git", "-C", p, "push"],
]
out = []
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True)
    out.append(f"RC {r.returncode} :: {c[-1]}\nOUT {r.stdout[-500:]}\nERR {r.stderr[-500:]}")
with open("/tmp/rank82_commit.txt", "w") as f:
    f.write("\n".join(out))
