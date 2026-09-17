import subprocess, time
ts = time.strftime("%Y-%m-%d %H:%M")
msg = f"falsify 第54回: K-Z3 17時台 n 積み増し run155A-C (cold 4/1/0 per 20 = 5/60 ~8.3%, search のみ 1s 超外れ値, control 静穏 p50 53ms) evidence 追記 — status 遷移なし"
for cmd in [
    ["git", "add", "query-cosientist.md", "kz3_run155.sh", "kz3_run155_out.txt",
     "kz3_run155_calc.py", "kz3_run155_calc.txt", "fz155_append.py"],
    ["git", "commit", "-m", msg],
    ["git", "push", "net-kotobase", "HEAD:main"],
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print("$", " ".join(cmd), "rc=", r.returncode)
    print(r.stdout[-500:], r.stderr[-500:])
