#!/usr/bin/env python3
# bench 第196回: append K-Z3 run472 evidence + insertion log entry (anchor-based)
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
raw = open(p, encoding="utf-8").read()
lines = raw.split("\n")

# ---- evidence block append: insert new evidence line just BEFORE "## Iteration log" ----
ev = (" bench 2026-09-08 (第196回, K-Z3 14時台 n 積み増し run472A–C — rank 第211回 NEXT「K-Z3 14時台 n-add run472」"
      " に従い 14時台 3 セット目 (falsify run470 帯初 5/60 + bench run471 1/60 済の続行枠), 同測定法 n=20 × 3 + landing control, 別接続 curl,"
      " cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 14:22–14:24 JST, 全 80/80 200,"
      " host load1 17.10 (14:22 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ):"
      " cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — run472A 散発クラスタ 5/20 (pos1 1.1597s / pos5 1.8436s / pos7 1.0192s / pos8 1.0141s / pos11 1.0958s"
      " — 冒頭 1 + 中盤隣接ペア 7/8 + 散発 5/11, warm 群 0.043–0.128s) p50 56.8ms max 1843.6ms / run472B cold 0/20 p50 46.2ms max 174.6ms /"
      " run472C cold 0/20 p50 44.9ms max 127.1ms, control (kotobase.net/signup) cold 0/20 p50 43.6ms max 136.9ms 完全静穏で control 分離成立、"
      " cold 群は search 側に局在。run472A 散発 5/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ型継続"
      " (run471A 単発 1/20 → 本 tick 5/20 の再上振れ, heavy>=6/20 は 14時台帯初 5/20 未達のまま非再現継続)。"
      " 14時台 (9/8) 通算 = falsify run470 (5/60, 帯初) + bench run471 (1/60) + 本 tick run472 (5/60) = 11/180 (~6.1%) の 3 セット中位帯候補"
      " — 帯初再上振れ (5/60) → 帯内減衰 (1/60) → 再上振れ (5/60) の振幅、日中帯セット間変動大継続 (traffic 依存説の日中帯方向支持継続,"
      " 深夜帯 ~26-31% 平坦パターンとの対比不変)。帯 n=3 セットで帯水準確定・機構判断には rank 追加 n を要する。"
      " status 判定は rank に委ねる (rank 専門)。")

# ---- iter-log entry (newest first) ----
it = ("- 2026-09-08: bench 第196回。14:26 JST tick。HEAD 04fdafd = rank 第211回 (14:14, K-Z3 14時台 fold run470"
      "(falsify 5/60 帯初)+run471(bench195 1/60) -> 6/120 ~5.0% 2セット; NEXT K-Z3 14時台 n-add run472)"
      " = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込;"
      " terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」"
      " は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第211回「K-Z3 14時台 n-add run472」))。"
      " 本 tick は rank 第211回 NEXT に従い 14時台 3 セット目 run472A–C を実施。live smoke 200 (/, /signup; pre-run 計測)。"
      " host load1 17.10 (14:22 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
      " K-Z3 14時台 run472A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50,"
      " 正 endpoint search.kotobase.net/search?q=test, 14:22–14:24 JST, 全 80/80 200, secret 不含 — curl + python stats のみ):"
      " cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — run472A 散発クラスタ 5/20 (pos1 1.1597s / pos5 1.8436s / pos7 1.0192s / pos8 1.0141s / pos11 1.0958s)"
      " p50 56.8ms max 1843.6ms / run472B cold 0/20 p50 46.2ms max 174.6ms / run472C cold 0/20 p50 44.9ms max 127.1ms,"
      " control (kotobase.net/signup) cold 0/20 p50 43.6ms max 136.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
      " run472A 散発 5/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ型継続 (run471A 単発 1/20 → 本 tick 5/20 再上振れ,"
      " heavy>=6/20 は 14時台帯初 5/20 未達のまま非再現)。14時台 (9/8) 通算 = falsify run470 (5/60, 帯初) + bench run471 (1/60) + 本 tick run472 (5/60)"
      " = 11/180 (~6.1%) の 3 セット中位帯候補 — 帯初再上振れ → 帯内減衰 → 再上振れの振幅、日中帯セット間変動大継続 (traffic 依存説の日中帯方向支持継続,"
      " 深夜帯 ~26-31% 平坦パターンとの対比不変)。帯 n=3 セットで帯水準確定・機構判断には rank 追加 n を要する。"
      " status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (末尾追記)。"
      " NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run473)。")

# locate "## Iteration log" header (unique)
hdr_idx = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        hdr_idx = i
        break
if hdr_idx is None:
    raise SystemExit("ITER HDR not found")

# 1) evidence block append: insert ev line before header
lines.insert(hdr_idx, ev)
hdr_idx += 1

# 2) iter-log entry: insert after the blank line following the header
# after step 1, lines[hdr_idx] == "## Iteration log", lines[hdr_idx+1] == "" (blank)
target = hdr_idx + 2  # first entry position
lines.insert(target, it)

open(p, "w", encoding="utf-8").write("\n".join(lines))
with open("/tmp/b472_done.txt", "w", encoding="utf-8") as f:
    f.write("insert_ok hdr_idx_was=%d\n" % (hdr_idx-1))
print("ok")