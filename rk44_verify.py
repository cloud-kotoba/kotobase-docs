import subprocess
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r = subprocess.run(["git","fetch","net-kotobase"], capture_output=True, text=True, cwd=cwd)
r2 = subprocess.run(["git","rev-parse","net-kotobase/main"], capture_output=True, text=True, cwd=cwd)
r3 = subprocess.run(["git","rev-parse","HEAD"], capture_output=True, text=True, cwd=cwd)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_verify_out.txt","w").write(
    "remote main: %s\nHEAD: %s\n" % (r2.stdout.strip(), r3.stdout.strip()))
print("ok")
