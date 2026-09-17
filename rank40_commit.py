import subprocess, io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(cmd):
    r = subprocess.run(cmd, cwd=p, capture_output=True, text=True)
    return r.stdout + r.stderr

out = run(["git", "add", "query-cosientist.md"])
out += run(["git", "commit", "-m", "rank 第40回: bench 第40回 K-Q1 計測第2段 (K-Q2 harness 再使用 TTFB/total 分解: authed warm p50 656.70/654.61ms, TTFB≈total — gateway auth check 20.11/21.31ms との差分 ~635ms が backend 実行区間に帰属, 2 run 再現 — 退行主体 engine/KV 側で確定) と K-Z3 (run114A-C 5時台 0/60, cosientist run105A-C 6時台, bench run115A-C 6時台 0/60 — 深夜通算 95 試行中 29 ~30.5%) を取り込み, rank ブロック第40回版へ差替え (順位変動なし) + Iteration log 第40回 + NEXT (K-Z3 6時台 n 積み増し継続)"])
out += run(["git", "push"])
out += run(["git", "log", "--oneline", "-2"])
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank40_commit_out.txt", "w").write(out)
print("done")
