#!/usr/bin/env python3
import io, sys

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# --- Build the new K-Z3 evidence line (inserted after run230 evidence line) ---
new_ev = (
" bench 2026-09-06 (第95回, K-Z3 18時台 n 積み増し run231A\u2013C, 同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 18:17:34\u201318:18:30 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 111.84 (18:18 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 \u2014 rank 第97回 NEXT\u300cK-Z3 18時台 n 積み増し継続\u300dに従い 18時台で実施; \u203b falsify 第100回 run230 (18:03, 同 18時台) と ID 衝突を回避し run231, 独立 2 計測として採用可否は rank 判定に委ねる): cold(>=0.5s) 2/0/1 per 20 = 3/60 (~5.0%) \u2014 run231A 散発 2 件 (1.1288s 3番目 / 1.1466s 11番目) p50 166.5ms / run231B 0/20 p50 127.5ms max 232.1ms / run231C 単発 1 件 (0.9581s 2番目) p50 165.1ms, control (kotobase.net/signup) cold 0/20 p50 106.7ms max 337.7ms 静穏で control 分離成立、cold 群は search 側に局在 \u2014 falsify run230 の control borderline not-separated (control cold 1 件) は本 tick では非再現 (control 0/20) で分離成立。\u203b本 tick 全体の p50 (127\u2013167ms) は host load 高騰 (111.84) tick の全体的上振れ込みだが cold 3 件 (0.958\u20131.147s) は閾値決定的で cold 濃度判定 3/60 に影響なし (borderline note)。run231A 散発 2 件 + C 単発 1 件は A 内即消失 (B 0/20) し run222A/223A/225A/B/228A/B/C/229A/230B 型\u300c帯内 1 窓即消失\u300dパターン継続 \u2014 18時台 2 セット目 (run230 1/60 + run231 3/60) で 4/120 (~3.3%) の低位帯候補、17時台 (10/240 ~4.2%) と同水準の継続低温帯パターン (traffic 依存説の方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比も維持)。status 判定は rank に委ねる (rank 専門)。\n"
)

## Insert the new evidence line after the falsify 第100回 run230 evidence line.
anchor_run230 = "falsify 2026-09-06 (第100回, K-Z3 18時台 n 積み増し run230A\u2013C"
idx_run230 = None
for i, ln in enumerate(lines):
    if ln.startswith(anchor_run230):
        idx_run230 = i
        break
assert idx_run230 is not None, "run230 evidence anchor not found"
# Insert after that line (which is a complete paragraph ending with \n)
lines.insert(idx_run230 + 1, new_ev)

# --- Add iteration-log entry at the top of the Iteration log (right after "# Iteration log" heading) ---
new_iter = (
"- 2026-09-06: bench 第95回。18:10 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み (fetch rc 0, HEAD 1162ebf = fetch 後 net-kotobase/main 先端一致, 乖離 0)。falsify 第100回 (18:03, run230, 18時台) と rank 第97回 (18:02, NEXT\u300cK-Z3 18時台 n 積み増し継続\u300d) を取り込み済み確認。live smoke 200 (/, /signup; pre-run 計測)。host load1 111.84 (18:18 実測, gate 7.5 大幅超過) のため local 測定は拒否し\u300chost busy (load1 111.84)\u300dを記録。フォールバック (production HTTP 実測, gate 外): K-Z3 18時台 n 積み増し run231A\u2013C (rank 第97回 NEXT\u300cK-Z3 18時台 n 積み増し継続\u300dに従い 18時台を実施; ※ falsify 第100回 run230 と ID 衝突回避のため run231, 独立 2 計測として採用可否は rank 判定に委ねる; 同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, 18:17:34\u201318:18:30 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 2/0/1 per 20 = 3/60 (~5.0%) \u2014 run231A 散発 2 件 (1.1288s 3番目 / 1.1466s 11番目) p50 166.5ms / run231B 0/20 p50 127.5ms / run231C 単発 1 件 (0.9581s 2番目) p50 165.1ms, control (kotobase.net/signup) cold 0/20 p50 106.7ms max 337.7ms 静穏で control 分離成立、cold 群は search 側に局在 (falsify run230 の control borderline not-separated は非再現)。\u203b本 tick 全体の p50 (127\u2013167ms) は host load 高騰 (111.84) tick の全体的上振れだが cold 3 件 (0.958\u20131.147s) は閾値決定的 (borderline note)。run231A 散発 + C 単発は B 0/20 で即消失し run222A/\u2026/230B 型\u300c帯内 1 窓即消失\u300dパターン継続、18時台 2 セット目 4/120 (~3.3%) 低位帯候補 (17時台 10/240 ~4.2% と同水準)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n"
)

# Find "# Iteration log" heading
idx_log = None
for i, ln in enumerate(lines):
    if ln.strip() == "# Iteration log" or ln.strip() == "## Iteration log":
        idx_log = i
        break
assert idx_log is not None, "Iteration log heading not found"

# Insert new iteration entry after heading (before whatever follows). Newest-first: insert right after heading.
lines.insert(idx_log + 1, new_iter)

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("INSERT_OK")