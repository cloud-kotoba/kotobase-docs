import subprocess
# Diagnose: what SHA does deploy-versioned.mjs actually see as HEAD when run via subprocess from repo root?
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["git", "-c", "core.fsmonitor=false", "rev-parse", "HEAD"],
                   cwd=repo, capture_output=True, text=True, timeout=30)
out = "RC=%d\nstdout=%s\nstderr=%s\n" % (r.returncode, r.stdout, r.stderr)
r2 = subprocess.run(["node", "scripts/deploy-versioned.mjs"], cwd=repo, capture_output=True, text=True, timeout=60)
out += "usage_rc=%d\nstdout=%s\nstderr=%s\n" % (r2.returncode, r2.stdout, r2.stderr)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_diag_subprocess.txt", "w").write(out)
print("done")
