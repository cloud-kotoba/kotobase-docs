import subprocess
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
out = []
cmds = [
    ["git","add","query-cosientist.md"],
    ["git","commit","-m","rank 第44回: K-Q1 falsify 第3段取り込み (warm p50 683.73ms, auth plane ~28ms 分離で退行分 ~+470ms が backend query 実行区間に帰属確定 — engine/KV 側で切り分け完了, 残る切れ手は engine 内訳のみ) + bench 第45回 run125 (K-Z3 10時台初計測 cold 1/60) を K-Z3 記述に追加 — rank ブロック第44回版へ差替え, 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2), status 遷移なし。NEXT: K-Q1 engine 内訳の cosientist 実装指定"],
    ["git","push","net-kotobase","HEAD:main"],
]
for cmd in cmds:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    out.append("$ " + " ".join(cmd))
    out.append((r.stdout or "") + (r.stderr or ""))
    out.append("---")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_push_out.txt","w").write("\n".join(out))
print("done")
