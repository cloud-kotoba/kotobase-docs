import subprocess, time, datetime
# minimal: fire 3 curls immediately, log results
res = []
for i in range(3):
    r = subprocess.run(["/usr/bin/curl", "-s", "-o", "/dev/null", "-w", "%{time_starttransfer} %{http_code}",
                        "--max-time", "10", "https://search.kotobase.net/search?q=test"],
                       capture_output=True, text=True)
    res.append(r.stdout.strip())
    time.sleep(0.2)
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench38_mini.txt", "w") as f:
    f.write("t=%s\n%s\n" % (datetime.datetime.now().astimezone().strftime("%H:%M:%S"), "\n".join(res)))
