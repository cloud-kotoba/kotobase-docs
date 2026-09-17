#!/usr/bin/env python3
# falsify 第169回 insert: K-Z3 20hr n-add run395 evidence + iter-log entry
# plain UTF-8, direct characters (run366 pitfall: no unicode_escape decode)

MD = "query-cosientist.md"

iter_head = "- 2026-09-07: falsify 第169回。20:49 JST tick。HEAD 0ca3490 = rank 第168回 (20:39, fold bench175-run392 + falsify168-run393 + bench176-run394 → K-Z3 20時台 3 セット 10/180 ~5.6% 中位〜低位帯候補, NEXT K-Z3 20hr n-add run395) = remote bench_fetch/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 25.50 (20:49 pre-run uptime 実測, gate 7.5 大幅超過) — K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (rank 第168回)「K-Z3 20時台 n 積み増し続行、次 run ID は run395 使用」の run395 枠を本 tick 実施 (20時台 4 セット目, run392 7/60 + run393 2/60 + run394 1/60 済みの積み増し, run395 は commit 未使用で衝突なし確認)。K-Z3 20時台 run395A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:52 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 5/2/0 per 20 = 7/60 (~11.7%) — run395A cold 5/20 散発クラスタ (1.4014s/1.0582s/1.1819s/1.2318s/1.7538s 散発配置) p50 0.0915s max 1.7538s / run395B cold 2/20 (1.0602s/2.1259s) p50 0.0883s max 2.1259s / run395C cold 0/20 p50 0.0605s max 0.2119s, control (kotobase.net/signup) cold 0/20 p50 0.0560s max 0.1688s 完全静穏で control 分離成立、cold 群は search 側に局在。run395A 5/20 + B 2/20 は C+control 0/40 即消失で「帯内 1 窓即消失」散発クラスタ型継続 — run394A 単発 1/20 (20:22) の 30 分後再上振れ (heavy>=6/20 は未達, A/B の冷却即降下)。20時台 (9/7) 通算 = run392 7/60 + run393 2/60 + run394 1/60 + 本 tick run395 7/60 = 17/240 (~7.1%) の 4 セット中位帯候補 — 19hr (~8.0%)・18hr (~7.3%)・17hr (~7.5%) と同水準の帯横断継続 (日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run396 使用 — ※sibling bench/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)。"

evidence = " falsify 2026-09-07 (第169回, K-Z3 20時台 n 積み増し run395A–C — rank 第168回 NEXT「K-Z3 20hr n-add run395」の run395 枠を本 tick 実施 (20時台 4 セット目, run392 7/60 + run393 2/60 + run394 1/60 済みの積み増し, run395 は commit 未使用で衝突なし確認), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:52 JST, 全 80/80 200, host load1 25.50 (20:49 pre-run uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 5/2/0 per 20 = 7/60 (~11.7%) — run395A cold 5/20 散発クラスタ (1.4014s/1.0582s/1.1819s/1.2318s/1.7538s 散発配置) p50 0.0915s max 1.7538s / run395B cold 2/20 (1.0602s/2.1259s) p50 0.0883s max 2.1259s / run395C cold 0/20 p50 0.0605s max 0.2119s, control (kotobase.net/signup) cold 0/20 p50 0.0560s max 0.1688s 完全静穏で control 分離成立、cold 群は search 側に局在。run395A 5/20 + B 2/20 は C+control 0/40 即消失で「帯内 1 窓即消失」散発クラスタ型継続 — run394A 単発 1/20 (20:22) の 30 分後再上振れ (heavy>=6/20 は未達, A/B の冷却即降下)。20時台 (9/7) 通算 = run392 7/60 + run393 2/60 + run394 1/60 + 本 tick run395 7/60 = 17/240 (~7.1%) の 4 セット中位帯候補 — 19hr (~8.0%)・18hr (~7.3%)・17hr (~7.5%) と同水準の帯横断継続 (日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"

def scrub(s):
    return s.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "").replace("\ufeff", "")

iter_head = scrub(iter_head)
evidence = scrub(evidence)

with open(MD, encoding="utf-8") as f:
    text = f.read()

# 1. iter-log: insert new entry right after the header, before rank 第168回
anchor_header = "## Iteration log\n- 2026-09-07: rank 第168回"
assert anchor_header in text, "anchor_header not found"
text = text.replace(anchor_header, "## Iteration log\n" + iter_head + "\n- 2026-09-07: rank 第168回", 1)

# 2. K-Z3 evidence: append at end of the | K-Z3 | worker | hypothesis line
kz3 = "| K-Z3 | worker |"
idx = text.index(kz3)
end = text.index("\n", idx)  # end of that line
text = text[:end] + evidence + text[end:]

with open(MD, "w", encoding="utf-8") as f:
    f.write(text)

print("insert OK; chars=%d" % len(text))