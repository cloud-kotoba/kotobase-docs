import subprocess, io, re
def run(args, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()
rc, main = run(["git", "show", "net-kotobase/main:query-cosientist.md"])
lines = main.split("\n")
kz3 = next(ln for ln in lines if ln.startswith("| K-Z3 | worker |"))
# extract sentence mentioning run174
m = re.findall(r"bench 2026-09-05 \(第60回[^)]*\)[^|]*?(?= bench 2026| falsify| cosientist| \||$)", kz3)
out = ["MAIN run174 snippet: " + (m[0][:800] if m else "not found in row")]
# iteration log entry in main
entry = [ln for ln in lines if "bench 第60回" in ln and ln.startswith("- 2026-09-05")]
out.append("MAIN log entry: " + (entry[0][:800] if entry else "none"))
local = io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read()
out.append("LOCAL == MAIN: %s" % (local == main))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_gitdiag6.txt", "w", encoding="utf-8").write("\n\n".join(out))
