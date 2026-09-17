import subprocess, time, datetime
try:
    r = subprocess.run(["/usr/bin/python3", "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench38_z2.py"],
                       capture_output=True, text=True, timeout=280)
    out = "rc=%s\nstdout:\n%s\nstderr:\n%s\n" % (r.returncode, r.stdout, r.stderr)
except Exception as e:
    out = "EXC: %r\n" % (e,)
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench38_run2.txt", "w") as f:
    f.write(out)
