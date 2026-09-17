import subprocess, time, os
p = subprocess.Popen(["bash", "-x", "kz3_run107.sh"],
                     stdout=open("kz3_trace2.txt", "w"),
                     stderr=subprocess.STDOUT,
                     cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
time.sleep(8)
p.terminate()
time.sleep(1)
with open("kz3_trace2.txt", "a") as f:
    f.write("\n[terminated after 8s]\n")
print("rc", p.returncode)
