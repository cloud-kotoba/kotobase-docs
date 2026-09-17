#!/usr/bin/env python3
# bench 第175回 insert: K-Z3 20hr band-first run392 evidence + iter-log entry
# plain UTF-8, direct characters (run366 pitfall: no unicode_escape decode)

MD = "query-cosientist.md"

iter_head = "- 2026-09-07: bench 第175回。20:09 JST tick。HEAD f0e177b = rank 第167回 (20:08, K-Z3 19hr 5-set fold run391 24/300 ~8.0% 中位帯候補, NEXT K-Z3 20hr band-first run392) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 48.07 (20:08 pre-run uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (rank 第167回, 20:08)「委ねる (rank 指定優先; falsify/bench フォールバックは K-Z3 20時台帯初計測)」の run392 枠を本 tick 実施 (20時台帯初計測, 19時台 run387..run391 5 セット 24/300 ~8.0% 完了後の帯移行, run392 は commit 未使用で衝突なし確認)。K-Z3 20時台 run392A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:14:35–20:15:13 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 6/1/0 per 20 = 7/60 (~11.7%) — run392A cold 6/20 heavy 冒頭集中クラスタ (1.1891s pos2 / 2.1915s pos3 / 1.0849s pos4 / 1.3536s pos5 / 2.1482s pos7 / 1.3595s pos9, deep cold 2.19s 含む) p50 0.1206s max 2.1915s warm 群 ~0.04–0.09s / run392B cold 単発 1/20 (1.1615s pos4) p50 0.0954s / run392C cold 0/20 p50 0.0946s max 0.2502s, control (kotobase.net/signup) cold 0/20 p50 0.0611s max 0.2866s 完全静穏で control 分離成立、cold 群は search 側に局在。run392A cold 6/20 heavy は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ型継続 — heavy(>=6/20) は run390A 6/20 (19:41) の 33 分後再達 (run271A 系 heavy 再現 direction, deep 2.19s)。20時台 (9/7) 帯初計測 = 7/60 (~11.7%) の 1 セット高位帯初期サンプル — 19時台 (~8.0%) と同水準の高位方向 (日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run393 使用 — ※sibling falsify/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)。"

evidence = " bench 2026-09-07 (第175回, K-Z3 20時台帯初計測 run392A–C — rank 第167回 NEXT「K-Z3 20hr band-first run392」に従い現時刻帯 20時台帯初計測 (19時台 5 セット 24/300 ~8.0% 完了後の帯移行), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:14:35–20:15:13 JST, 全 80/80 200, host load1 48.07 (20:08 pre-run uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 6/1/0 per 20 = 7/60 (~11.7%) — run392A cold 6/20 heavy 冒頭集中クラスタ (1.1891s pos2 / 2.1915s pos3 / 1.0849s pos4 / 1.3536s pos5 / 2.1482s pos7 / 1.3595s pos9 — 冒頭集中 4 連続 + 中盤散発 2 件, deep cold 2.19s 含む) p50 120.6ms / run392B cold 単発 1/20 (1.1615s pos4) p50 95.4ms max 1161.5ms / run392C cold 0/20 p50 94.6ms max 250.2ms, control (kotobase.net/signup) cold 0/20 p50 61.1ms max 286.6ms 完全静穏で control 分離成立、cold 群は search 側に局在。run392A cold 6/20 は heavy (>=6/20) 閾値再達の 20時台帯初初候補 (run390A heavy 6/20 型の再出現, run391A 4/20 の 19 分後再上振れ) — B/C 0/40 + control 0/20 即消失で「帯内 1 窓即消失」型維持 (heavy>=6/20 の帯内持続性は帯内追加 n で確認)。20時台 (9/7) 帯初計測 = 7/60 (~11.7%) の 1 セット高位帯初期サンプル — 19時台 (~8.0%) と同水準の高位方向で日中帯 traffic 依存説の方向支持継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"

with open(MD, encoding="utf-8") as f:
    text = f.read()

# 1. iter-log: insert new entry right after the header, before rank 第167回
anchor_header = "## Iteration log\n- 2026-09-07: rank 第167回"
assert anchor_header in text, "anchor_header not found"
text = text.replace(anchor_header, "## Iteration log\n" + iter_head + "\n- 2026-09-07: rank 第167回", 1)

# 2. K-Z3 evidence: append at end of the | K-Z3 | hypothesis line
kz3 = "| K-Z3 | worker |"
idx = text.index(kz3)
end = text.index("\n", idx)  # end of that line
text = text[:end] + evidence + text[end:]

with open(MD, "w", encoding="utf-8") as f:
    f.write(text)

print("insert OK; chars=%d" % len(text))