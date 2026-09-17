import io, sys

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with open(P, encoding="utf-8") as f:
    txt = f.read()

# ---- 1) Append run301 evidence to K-Z3 row ----
anchor = "deep-night 累計 run275..300 = 31/1560 (~2.0%) の 26 セットで低位帯水準継続 — 深夜最低帯 (traffic 最低) 4時台での cold 散発再出現は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
new_ev = (" bench 2026-09-07 (第124回, K-Z3 4時台 n 積み増し run301A–C — falsify 第137回 run300 (04:03) が 4時台帯初を先行実施済みの 4時台 n 積み増し (次 run ID run301), "
          "同測定法 n=20 × 3 + landing control, 別接続 curl, 04:08:52–04:09:02 JST, 全 80/80 200, "
          "正 endpoint search.kotobase.net/search?q=test, host load1 48.08 (04:09 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外): "
          "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run301A cold 単発散発 1.6133s (p50 44.4ms max 1613.3ms warm 群 0.04s 帯と交互), "
          "run301B cold 0/20 p50 45.9ms max 99.7ms, run301C cold 0/20 p50 46.8ms max 126.9ms, "
          "control (kotobase.net/signup) cold 0/20 p50 46.2ms max 88.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
          "run301A 単発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (falsify run300 4時台帯初の単発再出現, heavy クラスタは run271A 6/20 以降 27 セット非再現)。"
          "4時台通算 (falsify run300 1/60 + 本 tick 1/60) = 2/120 (~1.7%) の 2 セット、deep-night 累計 run275..301 = 32/1620 (~2.0%) の 27 セットで低位帯水準継続 — "
          "深夜最低帯 (traffic 最低) 4時台での cold 散発再出現は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
          "帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")

cnt = txt.count(anchor)
if cnt != 1:
    print(f"KZ3 ANCHOR COUNT={cnt} (expected 1) - ABORT", file=sys.stderr)
    sys.exit(2)
txt = txt.replace(anchor, anchor + new_ev, 1)

# ---- 2) Insert iteration log entry after "## Iteration log" ----
ilog_anchor = "## Iteration log\n"
cnt = txt.count(ilog_anchor)
if cnt != 1:
    print(f"ITERLOG ANCHOR COUNT={cnt} (expected 1) - ABORT", file=sys.stderr)
    sys.exit(2)
entry = (
"- 2026-09-07: bench 第124回。04:10 JST tick。HEAD f66c43d = falsify 第137回 (run300A-C, 04:03, 4時台帯初計測, cold 1/60) "
"= remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 40.72 (04:07 pre-run) → 48.08 (04:09 uptime 実測, gate 7.5 大幅超過) "
"のため local 測定は拒否し production HTTP フォールバック (gate 外)。委ねる NEXT の現時刻帯フォールバック継続として 4時台 n 積み増し run301A–C を実施 "
"(falsify 第137回 run300 が 4時台帯初を先行実施済みの 4時台 n 積み増し, 同測定法 n=20 × 3 + landing control, 別接続 curl, "
"04:08:52–04:09:02 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): "
"cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run301A 単発 1.6133s p50 44.4ms / run301B 0/20 p50 45.9ms / run301C 0/20 p50 46.8ms, "
"control (kotobase.net/signup) cold 0/20 p50 46.2ms max 88.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
"run301A 単発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (falsify run300 4時台帯初の単発再出現, heavy クラスタは run271A 6/20 以降 27 セット非再現)。"
"4時台通算 (falsify run300 1/60 + 本 tick 1/60) = 2/120 (~1.7%) の 2 セット、deep-night 累計 run275..301 = 32/1620 (~2.0%) の 27 セットで低位帯水準継続 — "
"深夜最低帯 (traffic 最低) 4時台での cold 散発再出現は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
"status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 4時台 n 積み増し継続、次 run ID は run302 使用)。"
"※pre-run monitor NEXT「深夜帯 23時台」は rank 第90回帯 stale スナップショット (rank 第114回で共有判断済み) — 真の NEXT は現時刻帯 4時台 n 積み増し継続。\n"
)
txt = txt.replace(ilog_anchor, ilog_anchor + entry, 1)

with open(P, "w", encoding="utf-8") as f:
    f.write(txt)
print("INSERT-OK: KZ3 evidence + iterlog entry applied")