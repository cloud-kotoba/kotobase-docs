# -*- coding: utf-8 -*-
# Append bench run477 evidence to K-Z3 cell tail (line 404 end) + insert iter-log entry after header (line 405)
import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

# ---- run477 evidence text (1 line, appended directly to end of line 404) ----
ev = (" bench 2026-09-08 (第207回, K-Z3 15時台 n 積み増し run477A–C — iter-log HEAD (cosientist 第143回 NEXT「委ねる, フォールバック K-Z3 現在時刻帯 n 積み増し続行」) の続行枠 (run475 帯初 7/60 + cosientist run476 5/60 済, run477 は run476 後の次の独立計測), "
      "同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 15:41JST付近 (~15:40–15:42), 全 80/80 200, host load1 18.52 (15:40 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): "
      "cold(>=0.5s) 6/1/0 per 20 = 7/60 (~11.7%) — run477A heavy 散発クラスタ 6/20 (1.0012s/1.0208s/1.0357s/1.1119s/1.2847s/1.5369s 散発配置) p50 72.3ms max 1536.9ms / run477B cold 単発 1/20 (1.9464s) p50 52.7ms max 1946.4ms / run477C cold 0/20 p50 48.8ms max 135.9ms, "
      "control (kotobase.net/signup) cold 0/20 p50 56.5ms max 261.6ms 完全静穏で control 分離成立、cold 群は search 側に局在。run477A heavy 6/20 は B 1/20 + C 0/20 + control 0/20 で「帯内 1 窓即消失」heavy 寄り散発クラスタ型 (run475A heavy 6/20 の 24 分後再上振れ + run476A 散発 4/20 直後の heavy 再出現, heavy>=6/20 の帯水準持続は 15時台 3 セットで散発). 15時台 (9/8) 通算 = bench run475 (7/60, 帯初) + cosientist run476 (5/60) + 本 tick run477 (7/60) = 19/180 (~10.6%) の 3 セット中〜高位帯候補 — 帯初再上振れ (7/60) → 5/60 → 7/60 (heavy 再上振れ) の振幅、日中帯 high 側継続で traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。")

# append to end of line 404 (index 403) — strip existing trailing newline, concatenate, re-add newline
lines[403] = lines[403].rstrip("\n") + ev + "\n"

# ---- iter-log entry: insert right after '## Iteration log' header (line 405, index 404) ----
iter_entry = ("- 2026-09-08: bench 第207回。15:41 JST tick。HEAD ef1f80a = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact 前例で既知) — true progressive NEXT は iter-log HEAD 連鎖 (cosientist 第143回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行)」))。本 tick 開始時に worktree に cosientist 第143回 の iter-log 未 commit 編集 (mtime 15:30) を検知 — run476 (cosientist 第143回が 15:26 計測・iter-log のみ記録済, evidence 欄未追記) は既 claim のため重複測定せず、次の run477 を 15時台 n 積み増し 3 セット目として実施 (detached push にて cosientist 未 commit 行と併せ commit)。live smoke 200 (/, /signup; pre-run 計測 + 本 tick 実測 search/signup 200)。host load1 18.52 (15:40 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。K-Z3 15時台 run477A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 15:40–15:42 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 6/1/0 per 20 = 7/60 (~11.7%) — run477A heavy 散発クラスタ 6/20 (1.0012s/1.0208s/1.0357s/1.1119s/1.2847s/1.5369s 散発配置) p50 72.3ms / run477B 単発 1/20 (1.9464s) p50 52.7ms / run477C cold 0/20 p50 48.8ms, control (kotobase.net/signup) cold 0/20 p50 56.5ms max 261.6ms 完全静穏で control 分離成立、cold 群は search 側に局在。run477A heavy 6/20 は「帯内 1 窓即消失」heavy 寄り散発クラスタ型 (run475A 6/20 の 24 分後 heavy 再上振れ + run476A 散発 4/20 直後の heavy 再出現, heavy>=6/20 の帯水準持続は 15時台 3 セットで散発型). 15時台 (9/8) 通算 = bench run475 (7/60, 帯初) + cosientist run476 (5/60) + 本 tick run477 (7/60) = 19/180 (~10.6%) の 3 セット中〜高位帯候補 — 帯初再上振れ → 5/60 → 7/60 (heavy 再上振れ) の日中帯 high 側継続、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L404 末尾) に追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行)。\n")

# find header line index (line 405) => index 404
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == "## Iteration log":
        hdr_idx = i
        break
assert hdr_idx is not None, "header not found"
# insert iter entry right after header
lines.insert(hdr_idx + 1, iter_entry)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("DONE ev_len=%d iter_lines=1" % len(ev))
