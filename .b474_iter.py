#!/usr/bin/env python3
# Insert falsify 第213回 iter-log entry as newest (line 407, before bench197), idempotent.
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
entry = (
"- 2026-09-08: falsify 第213回。15:05 JST tick。HEAD a009c86 = bench 第197回 (14:49, K-Z3 14時台 4 セット目 run473 cold 8/60 ~13.3% — run473A heavy 6/20 14時台初 heavy, control 境界 2/20 borderline not-separated) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第197回 NEXT フォールバック「K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run474」))。本 tick は run474A–C を 14時台 n 積み増し 5 セット目として実施 (bench 第197回 run473 完了後の続行枠, .b474 は run474 の測定ファイルで run ID 衝突なし確認)。live smoke 200 (/, /signup; pre-run 計測)。host load1 106.25 (14:45 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。K-Z3 14時台 run474A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 14:51:36–14:52:00 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 2/0/1 per 20 = 3/60 (~5.0%) — run474A 散発 2/20 (pos2 1.8646s / pos12 1.0389s) p50 147.9ms max 1864.6ms / run474B cold 0/20 p50 107.6ms max 367.5ms / run474C 単発 1/20 (pos9 1.6205s) p50 145.7ms max 1620.5ms, control (kotobase.net/signup) cold 1/20 (pos14 0.5409s — threshold ぎりぎりの境界値) p50 144.7ms max 540.9ms — control 境界 1 件で完全静穏不成立 borderline not-separated-leaning 注記 (search cold 3/60 が 1.04–1.86s で threshold 決定的。run474A/C 散発 3/60 は B 0/20 + control 境界 1 件で「帯内 1 窓即消失」型継続 (run473A heavy 6/20 (14:45) の 6 分後散発減弱 — 14時台初 heavy は帯内持続せず単一窓即消失, heavy>=6/20 の帯水準持続は 4 セットで未確認のまま)。14時台 (9/8) 通算 = falsify run470 (5/60, 帯初) + bench run471 (1/60) + bench run472 (5/60) + bench run473 (8/60) + 本 tick run474 (3/60) = 22/300 (~7.3%) の 5 セット中位帯候補 — 帯初 5/60 → 1/60 → 5/60 → 8/60 (heavy 再上振れ) → 3/60 の振幅、日中帯セット間変動大継続 (traffic 依存説の日中帯方向支持継続, 深夜帯 ~26–31% 平坦パターンとの対比不変)。qualify する新 evidence は 0 本 (K-Q1 は残留が cosientist 実装専任の動的切れ手 delegation-for-request のみ — 実装は測定で qualify するもののみ, 反証が先; K-Z2 は発火交互作用方向非一貫で介入保留; K-Z3 は観測継続; K-S1/K-S2 は evidence なし) のため実装対象なし — 観測 tick。本 tick control 境界 1 件 + host load 高騰混入は note として rank 判定に委ねる。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L404 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run475 使用)。"
)
with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
# sanity: line 405 = "## Iteration log", line 406 = blank, line 407 = bench197
assert lines[404].rstrip() == "## Iteration log", "not iter header: " + lines[404][:40]
assert lines[406].startswith("- 2026-09-08: bench 第197回"), "bench197 not at idx406: " + lines[406][:40]
if any("falsify 第213回" in l for l in lines):
    print("already-present")
else:
    lines.insert(406, entry)  # 0-indexed 406 becomes line 407 (before bench197); blank at 406 stays
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("inserted")
print("count213 =", len([l for l in lines if "falsify 第213回" in l]))
print("line407 head:", lines[406][:50] if len(lines) > 406 else "NA")