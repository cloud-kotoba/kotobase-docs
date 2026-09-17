import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

marker = "  戻った tick は K-Z3 深夜帯 0時台 n 積み増しを優先してよい)。\n"
assert src.count(marker) == 1, f"marker count={src.count(marker)}"

addition = """- 2026-09-05: bench 第36回。quiet-host tick (load1 5.65, 1:55 JST tick 開始実測,
  gate 7.5 未満) で rank 第35回追記 NEXT の K-Q1 local 測定 2 本を実施。
  新規 evidence (詳細は K-Q1 evidence 欄): (a) graph-for per-request 解決の local
  実測 p50 0.018ms — 退行に寄与せず切れ手(b)は棄却材料。(b) verify-session 1 hop
  実測 p50 11.81ms — 1 重化の削減上限 ≈ 12ms (退行の 1.3–1.6%, 下限) で
  verify-session 2 重化は退行の主因ではない。退行 +~700ms の主体は backend
  query path / KV 側と予測更新。status 遷移なし (rank 専門)。
  NEXT: 委ねる (rank 判断 — K-Q1 の次切れ手は backend query path の計測候補)。
"""

out = src + addition
io.open(path, "w", encoding="utf-8").write(out)
print("appended", len(addition), "chars; new total", len(out))
