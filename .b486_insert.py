# append bench 211 K-Z3 run486 evidence to K-Z3 row + iter-log bullet
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ENTRY = (
" bench 2026-09-08 (bench 第211回, K-Z3 17時台 n 積み増し run486A-C - falsify run485 "
"17時台帯初計測 (cold 6/60, control borderline not-separated) の直後の独立 2 セット目, "
"同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 17:28-17:31 JST, 全 80/80 200, "
"正 endpoint search.kotobase.net/search?q=test, host load1 44 (17:31 uptime 実測, "
"gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): "
"cold(>=0.5s) 5/0/1 per 20 = 6/60 (~10.0%) - run486A 散発クラスタ 5/20 "
"(1.0397s/1.0551s/1.0849s/1.1554s/1.8270s) p50 77.0ms / run486B cold 0/20 p50 51.4ms "
"max 143.2ms / run486C cold 単発 1/20 (1.0590s) p50 47.8ms max 1.059s, "
"control (kotobase.net/signup) cold 0/20 p50 53.0ms max 411.2ms 完全静穏で control 分離成立 "
"(falsify run485 の control borderline control cold 2/20 に対し本 tick は clean 分離, "
"search 側 cold 6 は 1.0-1.8s 帯で閾値決定的)。run486A 散発クラスタ 5/20 + run486C 単発は "
"run485 の 17時台帯内 cold 6/60 の 14 分後の同型再現。17時台 (9/8) 通算 = falsify run485 (6/60) "
"+ 本 tick run486 (6/60) = 12/120 (~10.0%) 2 セット - 16時台 (27/360 ~7.5%) 続く日中帯 high 側継続で "
"traffic 依存説の方向支持, 深夜帯 22-31% 平坦パターンとの対比維持。※ host load1 44 (高負荷 tick) 混入"
"汚染は production 計測ゆえ gate 外。status 判定は rank に委ねる (rank 専門)。")

txt = open(P, encoding="utf-8").read()
lines = txt.split("\n")

row_idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        row_idx = i
if row_idx is None:
    raise SystemExit("K-Z3 row not found")
base = lines[row_idx].rstrip("\r")
lines[row_idx] = base + ENTRY
print("K row idx", row_idx, "len", len(base), "->", len(base) + len(ENTRY))

ilog = ("- 2026-09-08: bench 第211回 K-Z3 17時台 n 積み増し run486A-C (falsify run485 17時台帯初計測 "
"cold 6/60 / control borderline の独立 2 セット目), 同測定法 全 80/80 200, cold 6/60 (~10.0%) "
"- run486A 散発クラスタ 5/20 + run486C 単発, control 0/20 完全静穏分離成立。17時台通算 "
"12/120 (~10.0%) 2 セットで 16時台 (7.5%) 続く日中高帯。evidence は K-Z3 仮説行に追記済み。")

lines.append(ilog.rstrip())
open(P, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print("wrote", len(lines), "lines")