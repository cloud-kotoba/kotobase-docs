import subprocess, json
cmds = {
 "git_head": ["git", "log", "--oneline", "-1"],
 "git_status": ["git", "status", "--short"],
 "date": ["date", "+%H:%M:%S %Z"],
 "uptime": ["uptime"],
}
out = {}
for k, c in cmds.items():
    p = subprocess.run(c, capture_output=True, text=True)
    out[k] = {"rc": p.returncode, "stdout": p.stdout, "stderr": p.stderr[:500]}
with open("/tmp/rank_out.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
