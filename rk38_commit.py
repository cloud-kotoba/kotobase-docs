# rank 第38回の編集を commit + push する。
import subprocess

DOCS = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args, **kw):
    r = subprocess.run(args, capture_output=True, text=True, cwd=DOCS, **kw)
    return r.returncode, (r.stdout + r.stderr).strip()

rc, out = run(["git", "add", "query-cosientist.md"])
print("add:", rc, out)
rc, out = run(["git", "commit", "-m",
    "rank 第38回: K-Z3 4時台 run112 反映 (深夜帯通算 86/29 ~33.7%), K-Z2 対比 5 源累計非一貫 (run110/111 同方向, run108/109 反証) 取り込み, rank ブロック第38回版へ差替え (K-Q1 に backend 計測具体手法を明記: gateway 経由 vs backend 直叩き比較 + TTFB/total 分解), NEXT: K-Q1 backend query path 計測第1段 (production HTTP で gate 外)"])
print("commit:", rc, out)
rc, out = run(["git", "push", "net-kotobase", "HEAD:main"])
print("push:", rc, out)
