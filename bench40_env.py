import os, subprocess
out = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench40_env_out.txt","w")
out.write("cwd: %s\n" % os.getcwd())
out.write("files: %s\n" % ", ".join(sorted(os.listdir("."))[:40]))
r = subprocess.run(["git","pull","--ff-only"], capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
out.write("git pull rc=%d out=%s err=%s\n" % (r.returncode, r.stdout.strip(), r.stderr.strip()))
out.close()
