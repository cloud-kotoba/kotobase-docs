import subprocess
r = subprocess.run(["curl", "-sS", "https://kotobase.net/"], capture_output=True, text=True, timeout=30)
html = r.stdout
with open(".b560_links.txt", "w") as f:
    f.write("HTTP bytes: %d\n" % len(html))
    import re
    hrefs = sorted(set(re.findall(r'href="([^"]*)"', html)))
    for h in hrefs:
        f.write(h + "\n")
