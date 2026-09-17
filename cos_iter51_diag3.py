import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
sha = "7dc62497d0ffe6c492c3b3b5510f1c12ad5a9fe9"
env = {"GIT_DIR": repo + "/.git", "GIT_WORK_TREE": repo, "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin",
       "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "-c", "core.fsmonitor=false", "rev-parse", "HEAD"], cwd=repo,
                   capture_output=True, text=True, timeout=30, env=env)
out = "with_GIT_DIR_env: RC=%d stdout=%s stderr=%s\n" % (r.returncode, r.stdout, r.stderr)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_diag3.txt", "w").write(out)
print("done")
