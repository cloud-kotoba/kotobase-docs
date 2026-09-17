import subprocess
cmds = [
    ["git", "add", "query-cosientist.md"],
    ["git", "commit", "-m",
     "cosientist 第60回: K-Z3 22時台 n 積み増し run173A-C evidence (cold 1/60, control 静穏) + K-Q1 deploy run 33964821723 queued 継続を確認 (gh 実査)"],
    ["git", "push", "net-kotobase", "cosient-sync-60:cosient-sync-60"],
]
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True)
    print(" ".join(c), "rc=", r.returncode)
    print(r.stdout.strip()[:800])
    print(r.stderr.strip()[:800])
