import subprocess, os
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
os.chdir(d)
def run(*args):
    r = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    return "RC=%d\n%s%s" % (r.returncode, r.stdout, r.stderr)

out = []
out.append(run("add", "query-cosientist.md", "bench53b_kz3.py", "bench53b_run163_out.json",
               "bench53b_run163_out.txt", "bench53b_detail.py", "bench53b_detail_out.txt",
               "bench53b_append.py", "bench53b_append_out.txt"))
msg = ("bench 第54回: K-Z3 19時台 n 積み増し run163A-C (search cold 4/60 ~6.7%, 全 1s 超で run163A 冒頭クラスタ, "
       "p50 61-106ms, landing control 静穏で control 分離成立, 19時台通算 4/180 ~2.2% 低位帯) evidence + iteration log 追記 — status 遷移なし")
out.append(run("commit", "-m", msg))
out.append(run("push", "net-kotobase", "HEAD:main"))
with open("bench53b_git_out.txt", "w") as f:
    f.write("\n===\n".join(out))
print("done")
