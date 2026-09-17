import subprocess
lines = []
for cmd in [
    ["git", "diff", "--stat"],
    ["git", "status", "--short"],
]:
    p = subprocess.run(cmd, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs",
                       capture_output=True, text=True)
    lines.append("$ " + " ".join(cmd))
    lines.append(p.stdout)
    if p.stderr:
        lines.append("STDERR: " + p.stderr)
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/git_status_out.txt", "w") as f:
    f.write("\n".join(lines))
