import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return "RC=%d\n%s%s" % (r.returncode, r.stdout, r.stderr)

out = []
msg = (
    "bench 第45回: K-Z3 10時台帯初計測 run125A-C (10:08 JST, cold 1/60 薄単発 1.042s, "
    "control 静穏 — cron 時刻 10時台のため帯逸脱, run105/run116/run120 前例に従い記録; "
    "9時台に近い低位, 平坦パターン帯別分布の裾の材料追加)"
)
out.append("== commit -- query-cosientist.md (pathspec commit) ==")
out.append(run(["git", "commit", "-m", msg, "--", "query-cosientist.md"]))
out.append("== log -1 ==")
out.append(run(["git", "log", "--oneline", "-1"]))
out.append("== status file ==")
out.append(run(["git", "status", "--porcelain", "--", "query-cosientist.md"]))
io.open(cwd + "/bench45_commit3.txt", "w").write("\n".join(out)[:8000])
print("done")
