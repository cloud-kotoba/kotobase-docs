import subprocess, time
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
msg = ("bench 第51回: K-Z3 17時台 n 積み増し run158A-C (cold 0/60 完全静穏, 17時台通算 180 試行中 1 試行 ~0.6% 低位帯維持, "
       "control 静穏, warm p50 63-107ms に上振れしたが cold なし) evidence 追記 — status 遷移なし")
for cmd in [["git", "add", "query-cosientist.md", "kz3_run156_out.txt", "kz3_run156_calc.txt",
             "bench51_append.py", "bench51_fetch.py", "bench51_times.py", "bench51_findanchor.py",
             "bench51_ctx.py", "bench51_row.py"],
            ["git", "commit", "-m", msg],
            ["git", "push", "net-kotobase", "HEAD:main"]]:
    r = subprocess.run(cmd, cwd=d, capture_output=True, text=True)
    print("$", " ".join(cmd), "rc=", r.returncode)
    print(r.stdout[-400:], r.stderr[-400:])
