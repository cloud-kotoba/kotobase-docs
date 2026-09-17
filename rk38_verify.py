# push 後の検証: HEAD/remote 状態と編集の反映を確認する。
import subprocess

DOCS = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=DOCS)
    return (r.returncode, (r.stdout + r.stderr).strip())

for args in (["git", "log", "--oneline", "-4"],
             ["git", "rev-parse", "net-kotobase/main"],
             ["git", "rev-parse", "HEAD"],
             ["git", "show", "--stat", "--oneline", "HEAD"]):
    rc, out = run(args)
    print("$", " ".join(args), "->", rc)
    print(out[:1200])
    print("---")

s = open(DOCS + "/query-cosientist.md", encoding="utf-8").read()
checks = [
    ("rank header v38", "rank (期待 gain × 確率, 2026-09-05 第38回):" in s),
    ("K-Q1 method specified", "gateway 経由 (認証済み /api read, K-Q2 harness) と" in s),
    ("K-Z2 five-source", "5 源累計で非一貫)。*/2" in s),
    ("K-Z3 86/29 rank", "86 試行中 29 試行 (~33.7%)" in s),
    ("K-Z3 4時台 rank", "4時台は bench 第38回 run112" in s),
    ("run112 evidence block", "第38回, K-Z3 深夜帯 4時台 n 積み増し run112" in s),
    ("iter log entry", "- 2026-09-05: rank 第38回。新規 evidence 3 本を取り込み。" in s),
    ("NEXT specified", "NEXT: K-Q1 backend query path 計測第1段" in s),
    ("old v37 header gone", "rank (期待 gain × 確率, 2026-09-05 第37回):" not in s),
    ("flat range updated", "(帯別 ~30–34% でほぼ平坦)" in s),
]
ok = True
for name, val in checks:
    print(("PASS " if val else "FAIL ") + name)
    ok = ok and val
print("ALL:", "OK" if ok else "FAILED")
