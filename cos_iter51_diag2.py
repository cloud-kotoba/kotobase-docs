import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
# Reproduce deploy()'s exact call sequence with spawnSync semantics from repo ROOT (like the script does).
r = subprocess.run(["node", "-e", "console.log(process.argv[1])", "noop"], cwd=repo, capture_output=True, text=True)
# Now emulate: script's run('git', [...], {capture:true}) uses spawnSync from cwd=ROOT (= repo root's parent? check)
# ROOT = path.resolve(BACKEND, "..") where BACKEND = engine dir => ROOT = orgs/net-kotobase
r2 = subprocess.run(["git", "-c", "core.fsmonitor=false", "rev-parse", "HEAD"],
                    cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase", capture_output=True, text=True, timeout=30)
out = "revparse_from_parent: RC=%d stdout=%s stderr=%s\n" % (r2.returncode, r2.stdout, r2.stderr)
ls = subprocess.run(["ls", "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase"], capture_output=True, text=True)
out += "ls_parent=%s\n" % ls.stdout
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_diag2.txt", "w").write(out)
print("done")
