# 修正分の commit + push + 検証。
import subprocess

DOCS = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=DOCS)
    return r.returncode, (r.stdout + r.stderr).strip()

rc, out = run(["git", "add", "query-cosientist.md"])
print("add:", rc, out)
rc, out = run(["git", "commit", "-m",
    "rank 第38回 (修正): falsify run112A-C (K-Z3 5時台, cold 1/60, control 静穏) を取り込み深夜帯通算を 89/29 (~32.6%) に更新, bench 第38回 4時台単体試行を run113 に改名 (falsify run112 との ID 衝突回避), rank/evidence/log の整合"])
print("commit:", rc, out)
rc, out = run(["git", "push", "net-kotobase", "HEAD:main"])
print("push:", rc, out)
rc, out = run(["git", "rev-parse", "HEAD"])
head = out
rc, out = run(["git", "rev-parse", "net-kotobase/main"])
print("HEAD==remote:", head == out)

s = open(DOCS + "/query-cosientist.md", encoding="utf-8").read()
checks = [
    ("rank run113 renamed", "4時台は bench 第38回 run113" in s),
    ("rank 89/29", "89 試行中 29 試行 (~32.6%)" in s),
    ("rank includes 5時台", "5時台は falsify run112A–C (cold 1/60, 薄単発, control 静穏)" in s),
    ("flat 29-34", "(帯別 ~29–34% でほぼ平坦)" in s),
    ("no old 86/29 rank", "86 試行中 29 試行" not in s),
    ("evidence run113", "run113 (※ falsify run112A–C との ID 衝突を回避し run113 とする)" in s),
    ("log run113 + run112A-C", "run113 に改名)" in s and "cold 1/60 薄単発" in s),
]
ok = True
for name, val in checks:
    print(("PASS " if val else "FAIL ") + name)
    ok = ok and val
print("ALL:", "OK" if ok else "FAILED")
