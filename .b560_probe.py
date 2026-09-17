import subprocess
for probe in ["https://kotobase.net/search?q=test",
              "https://search.kotobase.net/search?q=test",
              "https://search.kotobase.net/"]:
    r = subprocess.run(["curl", "-sS", "-o", "/dev/null",
                        "-w", "%{http_code} %{time_starttransfer} %{url_effective}",
                        probe], capture_output=True, text=True, timeout=30)
    with open(".b560_probe.txt", "a") as f:
        f.write(probe + " -> " + r.stdout.strip() + " " + r.stderr.strip()[:150] + "\n")
