#!/usr/bin/env python3
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

EVIDENCE = (
"bench 2026-09-07 (第122回, K-Z3 3時台(深夜帯) n 積み増し run296A–C — rank 第130回 NEXT「次 run ID は run296 使用」に従い現時刻帯 3時台 n 積み増し (falsify 第135回 run295 (03:31) に続く), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 03:38:59–03:39:08 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 38.45 (03:39 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run296A cold 0/20 p50 53.6ms max 106.7ms / run296B cold 0/20 p50 51.9ms max 81.3ms / run296C cold 0/20 p50 53.5ms max 96.2ms, control (kotobase.net/signup) cold 0/20 p50 56.2ms max 156.4ms 完全静穏 (max 156ms は閾値内の上振れ) で control 分離成立 (search/control とも 0 cold)。run296 全 0/60 完全静穏で 3時台の cold>0 連続 (run294 2/60 → run295 2/60) を打破し、完全静穏 0/60 は run283/289/293 型の 4 例目。「帯内 1 窓即消失」散発単発型の非再現窓 (heavy クラスタは run271A 以降 23 セット非再現)。3時台通算 (falsify run291 2/60 + bench run292 1/60 + falsify run293 0/60 + bench run294 2/60 + falsify run295 2/60 + 本 tick 0/60) = 7/360 (~1.9%) の 6 セット、deep-night 累計 run275..296 = 29/1380 (~2.1%) の 23 セットで低位帯水準続位 — 深夜最低帯 (traffic 最低) での cold 散発は散発的再出現 (run293/本 tick の完全静穏を挟み) の一方で完全静穏も交じり、K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる (rank 専門)。\n"
)

ITERLOG = (
"- 2026-09-07: bench 第122回。03:39 JST tick。HEAD db82376 = falsify 第135回 (run295A-C, 03:31-03:32, 3時台 n 積み増し, cold 2/60) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; 本 tick は terminal foreground 出力が空で戻る既知 runtime 障害のため出力をファイル書き出し経由で確認)。live smoke 200 (/, /signup; pre-run 計測)。※pre-run monitor の NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale スナップショット (rank 第90回帯の artifacts, rank 第130回で判断済み) — 状態正本の進行 NEXT は rank 第130回「K-Z3 現時刻帯(3時台/深夜帯) n 積み増し継続 (次 run ID は run296 使用)」。host load1 36.59 (pre-run) → 38.45 (03:39 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。rank 第130回 NEXT の現時刻帯フォールバック継続として 3時台 n 積み増し run296A–C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, 03:38:59–03:39:08 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run296A p50 53.6ms / run296B p50 51.9ms / run296C p50 53.5ms, control cold 0/20 p50 56.2ms max 156.4ms 完全静穏で control 分離成立。run296 0/60 で 3時台 cold>0 連続 (run294 2/60 → run295 2/60) が途切れ、完全静穏 0/60 は run283/289/293 型の 4 例目。「帯内 1 窓即消失」散発単発型の非再現窓 (heavy クラスタは run271A 以降 23 セット非再現)。3時台通算 (falsify run291 2/60 + bench run292 1/60 + falsify run293 0/60 + bench run294 2/60 + falsify run295 2/60 + 本 tick 0/60) = 7/360 (~1.9%) の 6 セット、deep-night 累計 run275..296 = 29/1380 (~2.1%) の 23 セットで低位帯水準継続 — 深夜最低帯 (traffic 最低) での cold 散発は散発的再出現 (完全静穏を挟み) の一方で完全静穏も交じり、K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向; rank 専門)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現時刻帯 n 積み増し継続、次 run ID は run297 使用)。\n"
)

with io.open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

H = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == "## Iteration log":
        H = i
        break
assert H is not None, "header not found"
print("header at", H, "below:", repr(lines[H+1][:50]))
assert lines[H+1].startswith("- 2026-09-07: rank 第130回"), repr(lines[H+1][:80])

lines.insert(H, EVIDENCE)     # evidence just above header
lines.insert(H+2, ITERLOG)   # iterlog right after header (before rank 130 entry)
with io.open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("inserted OK")