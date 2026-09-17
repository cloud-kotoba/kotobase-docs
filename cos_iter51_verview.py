import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
env = {"GIT_DIR": repo + "/.git", "GIT_WORK_TREE": repo, "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin",
       "HOME": "/Users/junkawasaki"}
r = subprocess.run(["npx", "wrangler", "versions", "view", "ea383ee7-0f9d-427b-8994-b2da566a05c2", "--env=", "--json"],
                   cwd=repo + "/..", capture_output=True, text=True, timeout=120, env=env)
out = "RC=%d\n" % r.returncode + r.stdout[:4000] + "\n---STDERR---\n" + r.stderr[-1000:]
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_verview.txt", "w").write(out)
print("rc", r.returncode)
