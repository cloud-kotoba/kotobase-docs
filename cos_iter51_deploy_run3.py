import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
sha = "7dc62497d0ffe6c492c3b3b5510f1c12ad5a9fe9"
env = {"GIT_DIR": repo + "/.git", "GIT_WORK_TREE": repo, "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin",
       "HOME": "/Users/junkawasaki"}
r = subprocess.run(["node", "scripts/deploy-versioned.mjs", "production", "--confirm-production", sha],
                   cwd=repo, capture_output=True, text=True, timeout=540, env=env)
out = "RC=%d\n" % r.returncode + r.stdout[-5000:] + "\n---STDERR---\n" + r.stderr[-3000:]
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_deploy_run3.txt", "w").write(out)
print("deploy rc", r.returncode)
