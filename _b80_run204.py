import subprocess, time

ENDPOINT = "https://search.kotobase.net/search?q=test"
CONTROL = "https://kotobase.net/signup"
GROUPS = ["run204A", "run204B", "run204C"]
N = 20

def probe(url):
    t0 = time.perf_counter()
    p = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url],
        capture_output=True, text=True, timeout=30,
    )
    dt = time.perf_counter() - t0
    code = p.stdout.strip() or "000"
    return code, dt

rows = []
for g in GROUPS:
    for i in range(1, N + 1):
        code, dt = probe(ENDPOINT)
        rows.append(f"{g} {i} {code} {dt:.6f}")
    time.sleep(2)

for i in range(1, N + 1):
    code, dt = probe(CONTROL)
    rows.append(f"ctrl {i} {code} {dt:.6f}")

with open("_b80_run204_out.txt", "w") as f:
    f.write("\n".join(rows) + "\n")
print("done", len(rows))
