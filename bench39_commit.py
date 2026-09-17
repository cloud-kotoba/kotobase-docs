import subprocess

msg = (
    "bench 第39回: K-Q1 backend query path 計測第1段 (engine 直叩きは DNS 不解決のため "
    "fallback 条項で gateway 単独分解: POST /api/q no-auth 402 応答 total p50 15.87ms / "
    "GET / 200 p50 13.09ms — gateway 前段 overhead は小さく退行は backend 実行区間寄りを "
    "下から支持; 実行区間計測には K-Q2 harness 再使用が次段) + Iteration log\n"
)
subprocess.run(["git", "add", "query-cosientist.md", "kq1_backend_stage1.mjs",
                "kq1_stage1_out.json"], check=True)
subprocess.run(["git", "commit", "-m", msg], check=True)
subprocess.run(["git", "push", "net-kotobase", "HEAD:main"], check=True)
print("pushed")
