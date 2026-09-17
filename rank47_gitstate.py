import subprocess, os

def run(args):
    r = subprocess.run(["git"] + args, capture_output=True, text=True,
                       cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    return (r.stdout + r.stderr).strip()

out = []
out.append("=== branch ===")
out.append(run(["branch", "--show-current"]))
out.append("=== HEAD ===")
out.append(run(["log", "--oneline", "-1"]))
out.append("=== branch -a ===")
out.append(run(["branch", "-a"]))
out.append("=== status head ===")
st = run(["status", "--short"])
out.append("dirty_files=" + str(len(st.splitlines())))
out.append("=== origin/main ===")
out.append(run(["log", "--oneline", "-3", "origin/main"]))
out.append("=== rev-parse HEAD vs origin/main ===")
out.append("HEAD=" + run(["rev-parse", "HEAD"]))
out.append("ORIG=" + run(["rev-parse", "origin/main"]))
print("\n".join(out))
