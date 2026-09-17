import subprocess, pathlib
p = pathlib.Path("query-cosientist.md")
t = p.read_text()
entry = "- 2026-09-06: rank 第71回。07:36 JST tick。worktree detached HEAD のため fetch net-kotobase + ancestor 比較で取り込み (fetch rc 0, HEAD 24eb7de = fetch 後 net-kotobase/main 先端一致, ancestor rc 0, 乖離 0)。※前 tick の rank 第70回 log entry が未 commit のまま working tree に残っていたため本 tick で commit に含める。rank 第70回 (c37950f, 07:02) 以降の新規 evidence は 2 本: bench 第71回 run191A–C (6時台, cold 1/60 単発, control 分離) + falsify 第72回 run192A–C (7時台帯初計測, cold 1/60 単発 0.935s, control borderline not-separated 傾向 — 本 tick 全体 p50 90–190ms は host load 高騰 tick の全体的上振れで cold 濃度判定 1/60 自体には影響なし)。取り込み判定: (a) K-Z3: run191 は 6時台低位帯 (~1-2%) 判定と整合し変動なし。7時台は帯初計測で control borderline のため採用性は限定的だが run188A/192A 型薄い単発で低位帯寄りの初期サンプル (単一サンプル, 追加 n 要)。run186A 群発 (9/20) 非再現は 5 tick 連続で継続 — run100A/116A/180A 型「帯内 1 窓即消失」パターン支持を維持。(b) K-Q1: 変化なし — transact 401 解決待ちの滞留継続 (write path 調査が KV read 内訳初実測の前提)。status 遷移なし (transition 要件を満たす canonical 測定なし: K-Q1 は transact 401 解決待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。NEXT: K-Q1 transact 401 (write path) の調査 (cosientist 実装担当; 期待利得最大, K-Q1 KV read 内訳実測の前提)。bench/falsify のフォールバックは K-Z3 7時台 n 積み増し継続。\n"
anchor = "## Iteration log\n"
idx = t.index(anchor) + len(anchor)
t = t[:idx] + entry + t[idx:]
p.write_text(t)
def git(*a): return subprocess.run(["git"]+list(a), capture_output=True, text=True)
print(git("add","query-cosientist.md").returncode)
c = git("commit","-m","rank 第71回: evidence 取り込み (bench71/falsify72 K-Z3 6-7時台), status 遷移なし, NEXT K-Q1 transact 401 調査")
print(c.returncode, c.stdout[-200:], c.stderr[-200:])
u = git("push","net-kotobase","HEAD:main")
print(u.returncode, u.stdout[-200:], u.stderr[-300:])
v = git("rev-parse","HEAD")
print("HEAD", v.stdout.strip())
