import subprocess
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
msg = ("bench 第52回: K-Q1 deploy 整合再確認 — cosientist 第51回再 deploy (ea383ee7, 7dc6249) 後も "
       "x-kotobase-kv-stats header 不在 60/60 (deployed: false), 空 graph warm query p50 329.77/331.40ms "
       "(bench 第49回 ~305ms と同水準, not-separated) evidence + iteration log 追記 — status 遷移なし")
files = ["query-cosientist.md", "bench52_kq1_out.json", "bench52_kq1_edge.mjs",
         "bench52_run.py", "bench52_mk.py", "bench52_append.py", "bench52_verify.py",
         "bench52_verify.txt", "bench52_kq1_err.txt", "bench52_run_out.txt",
         "bench52_run_out2.txt", "bench52_run_out3.txt", "bench52_run_out4.txt",
         "bench52_append_out.txt", "bench52_check.py", "bench52_ls.txt"]
for cmd in [["git", "add"] + files,
            ["git", "commit", "-m", msg],
            ["git", "push", "net-kotobase", "HEAD:main"],
            ["git", "log", "--oneline", "-1"]]:
    r = subprocess.run(cmd, cwd=d, capture_output=True, text=True)
    open("bench52_commit_out.txt", "a").write(
        "$ " + " ".join(cmd) + f" rc={r.returncode}\n{(r.stdout or '')[-300:]}{(r.stderr or '')[-300:]}\n")
