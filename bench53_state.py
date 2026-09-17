import subprocess, json
cmds = [
    ["date"],
    ["sysctl", "-n", "vm.loadavg"],
    ["git", "pull", "--ff-only"],
    ["git", "log", "--oneline", "-2"],
]
out = {}
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True, timeout=120,
                       cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    out[" ".join(c)] = (r.stdout.strip() + " " + r.stderr.strip()).strip()
print(json.dumps(out, ensure_ascii=False, indent=1))
