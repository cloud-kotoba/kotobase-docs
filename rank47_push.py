import subprocess

CWD = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    r = subprocess.run(["git"] + args, capture_output=True, text=True, cwd=CWD)
    return (r.stdout + r.stderr).strip()

print("=== add ===")
print(run(["add", "query-cosientist.md"]))
print("=== commit ===")
print(run(["commit", "-m",
  "rank 第47回: falsify 第51回 evidence 2 本取り込み (K-Z3 13時台 run151A-C cold 4/60 ~6.7% 低位散発型 — 12時台 ~8.3% と同程度 + K-Q1 PR #3 未 deploy 実測確認) — status 遷移なし, rank ブロック第47回版へ差替え (順位変動なし K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2), PR #3 deploy 承認 (観察専用計装, build/test 通過済み), NEXT: PR #3 cosientist deploy 実行 + deploy 後 x-kotobase-kv-stats header 読み取り付き同測定法計測"]))
print("=== push ===")
print(run(["push", "net-kotobase", "HEAD:main"]))
print("=== post-verify ===")
print(run(["log", "--oneline", "-1", "net-kotobase/main"]))
