import subprocess, json

CWD = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    r = subprocess.run(["git"] + args, capture_output=True, text=True, cwd=CWD)
    return (r.stdout + r.stderr).strip()

print("=== fetch ===")
print(run(["fetch", "net-kotobase"]))
print("=== remote main ===")
print(run(["log", "--oneline", "-3", "net-kotobase/main"]))
print("=== HEAD vs remote main ===")
print("HEAD :", run(["rev-parse", "HEAD"]))
print("MAIN :", run(["rev-parse", "net-kotobase/main"]))
