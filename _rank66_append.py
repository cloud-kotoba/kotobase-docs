import io

path = "query-cosientist.md"
entry = """- 2026-09-06: rank 第66回。04:48 JST tick。※worktree detached HEAD のため fetch net-kotobase main + ancestor 比較で取り込み (fetch rc 0, HEAD 40a6a5d = fetch 後 net-kotobase/main 先端と一致, ancestor rc 0, 乖離 0) — rank 第65回以降の新規 evidence は bench 第67回 (K-Z3 4時台 3 セット目 run184A–C: cold 0/0/0 per 20 = 0/60, control 静穏, 4時台通算 2/180 ~1.1% 低位帯) と falsify 第68回 (K-Z3 5時台帯初計測 run185A–C: cold 0/60 完全静穏, warm p50 33–35ms, control cold 0/20 p50 42ms 静穏で分離成立) の 2 本。取り込み判定: (a) K-Q1: 変化なし — transact 401 (3 例目, bench65 診断で authn chain 健全・transact endpoint 固有と確定済み) により KV read 内訳初実測 (非空 graph query + x-kotobase-kv-stats 値取得) は write path 調査 (cosientist 実装担当) を前提に滞留、open 維持。(b) K-Z3: 4時台は 3 セット通算 2/180 (~1.1%) で 5/6/8時台級の低位帯に確定寄り。5時台帯初計測 0/60 完全静穏は 9/5 の run112/114 (1/120) と整合し 5時台は深夜帯内で最静穏帯という判定を維持 — 深夜帯低位帯パターン (4/5/6/8時台 ~0-2%, 3時台は帯内 1 窗型 ~9% を含む) に整合、帯内 1 窗即消失型の解釈は不変。status 遷移なし (transition 要件を満たす canonical 測定なし: K-Q1 は transact 401 解決待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。NEXT: K-Q1 transact 401 (write path) の調査 — ephemeral EOA flow の transact endpoint 固有 401 の原因特定は K-Q1 非空 graph query KV read 内訳実測の前提であり期待利得最大 (cosientist 実装担当が適切; bench/falsify のフォールバックは K-Z3 5時台 n 積み増し継続)。
"""

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()
if "rank 第66回" in content:
    print("ALREADY_PRESENT")
else:
    with io.open(path, "a", encoding="utf-8") as f:
        f.write("\n" + entry)
    print("APPENDED")
