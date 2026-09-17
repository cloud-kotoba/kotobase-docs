import subprocess, os, json, re

CWD = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    r = subprocess.run(["git"] + args, capture_output=True, text=True, cwd=CWD)
    return (r.stdout + r.stderr).strip()

# c02871d (falsify 第51回) の commit 時刻を取得 — evidence の実行時刻の裏付け
print(run(["log", "-1", "--format=%ci %s", "c02871d"]))
