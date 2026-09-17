import subprocess
D = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
cmds = [
    ["git", "-C", D, "add", "query-cosientist.md"],
    ["git", "-C", D, "commit", "-m",
     "falsify 第51回: K-Z3 13時台 n 積み増し run151A-C (cold 4/60 ~6.7% 低位散発型, control 静穏 — 13時台帯初計測, 12時台 ~8.3% と同程度) + K-Q1 PR #3 未 deploy 確認 (x-kotobase-kv-stats header 不在, deploy 後計測は不可)"],
    ["git", "-C", D, "push", "net-kotobase", "HEAD:main"],
]
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/fz151_commit_out.txt", "w") as f:
    for c in cmds:
        r = subprocess.run(c, capture_output=True, text=True)
        f.write(f"$ {' '.join(c)}\nexit={r.returncode}\n{r.stdout}\n{r.stderr}\n---\n")
print("done")
