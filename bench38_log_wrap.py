import subprocess
r = subprocess.run(["/usr/bin/python3", "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench38_log.py"],
                   capture_output=True, text=True)
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench38_log_out.txt", "w") as f:
    f.write("rc=%s\nstdout:\n%s\nstderr:\n%s\n" % (r.returncode, r.stdout, r.stderr))
