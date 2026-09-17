import subprocess
msg = ("falsify: K-Q1 engine 内訳計測 第3段 (rank 第43回 NEXT, K-Q2 harness 10:29 JST): "
       "authenticated warm query p50 683.73ms / p95 995.39ms (200 30/30, NRT) — 第2段と同水準で退行存続。"
       "同窓 Biscuit verify p50 17.28ms / gateway auth check p50 10.78ms — auth plane 計 ~28ms で "
       "退行分 ~+470ms は backend query 実行区間に帰属確定、残る切れ手は engine KV read 内訳")
r = subprocess.run(["git", "add", "query-cosientist.md"], capture_output=True, text=True)
print("add:", r.returncode)
r = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
print("commit:", r.returncode, r.stdout[-200:], r.stderr[-300:])
r = subprocess.run(["git", "push", "net-kotobase", "HEAD:main"], capture_output=True, text=True)
print("push:", r.returncode, r.stdout[-300:], r.stderr[-300:])
r = subprocess.run(["git", "log", "--oneline", "-1"], capture_output=True, text=True)
print("head:", r.stdout.strip())
