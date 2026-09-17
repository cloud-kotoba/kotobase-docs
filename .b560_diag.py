import subprocess, time, statistics, json

samples = []
codes = []
for i in range(5):
    r = subprocess.run(["curl", "-sS", "-o", ".b560_body.html",
                        "-w", "%{http_code} %{time_starttransfer} %{time_total}",
                        "https://kotobase.net/search?q=test"],
                       capture_output=True, text=True, timeout=30)
    codes.append((r.stdout.strip(), r.stderr.strip()[:200]))
with open(".b560_diag.txt", "w") as f:
    f.write(repr(codes) + "\n")
