import subprocess

r = subprocess.run(["git", "add", "query-cosientist.md"], capture_output=True, text=True)
r2 = subprocess.run(["git", "commit", "-m",
    "bench 第58回 ID 読み替え: 21時台分 run170 → run171 (run170 は cosientist 第58回追記の run169 衝突読み替え分と重複のため, run167/168 前例)"],
    capture_output=True, text=True)
print("commit rc:", r2.returncode, r2.stderr[-200:] if r2.returncode else r2.stdout[-150:])
if r2.returncode == 0:
    r3 = subprocess.run(["git", "push"], capture_output=True, text=True)
    print("push rc:", r3.returncode)
    print((r3.stdout or "")[-200:], (r3.stderr or "")[-300:])
    r4 = subprocess.run(["git", "log", "-1", "--format=%H %s"], capture_output=True, text=True)
    print("HEAD:", r4.stdout.strip())
