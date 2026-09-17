#!/usr/bin/env python3
# bench 第163回 insert: append run372 evidence to K-Z3 line + iteration-log entry
import io, sys

F = "query-cosientist.md"
with io.open(F, encoding="utf-8") as fh:
    content = fh.read()

# --- 1) K-Z3 evidence cell: insert run372 note right before the final status/iter
# anchor: the unique run371 tail in the K-Z3 evidence cell (line 279)
anchor1 = "対比不変)。status 判定は rank に委ねる (rank 専門)。)"
kz3_note = (
    " bench 2026-09-07 (第163回, K-Z3 16時台 n-add run372, 同測定法 "
    "n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint "
    "search.kotobase.net/search?q=test, 16:36–16:40 JST, 全 80/80 200, "
    "host load1 33.73 (16:40 実測, production HTTP 実測のため gate 外), "
    "secret 不含 — curl のみ): cold(>=0.5s) 0/0/1 per 20 = 1/60 (~1.7%) — "
    "run372A cold 0/20 p50 55.2ms max 159.6ms / run372B cold 0/20 p50 47.6ms "
    "max 68.0ms / run372C cold 1/20 (2.0526s 末尾散発 単発) p50 46.2ms, "
    "control (kotobase.net/signup) cold 0/20 p50 43.8ms max 70.1ms 完全静穏で "
    "control 分離成立、cold 群は search 側に局在。run371A/B 2-run 跨散発 "
    "(8/60) の 16 時台 5 セット目として単発 1/60 で散発減弱 / 帯内 1 窓即消失型継続。"
    "16時台 (9/7) 通算 = run368 9/60 + run369 1/60 + run370 2/60 + run371 8/60 + "
    "本 tick run372 1/60 = 21/300 (~7.0%) の 5 セット高位帯候補 — "
    "帯内 heavy 単一窓 (run368A 8/20) の減衰・散発振幅 (8/60→1/60) を継続確認。"
    "status 判定は rank に委ねる (rank 専門)。"
)
assert content.count(anchor1) == 1, f"anchor1 count={content.count(anchor1)}"
content = content.replace(anchor1, kz3_note + anchor1, 1)

# --- 2) iteration log entry: insert after the bench 第162回 block (line 367)
iter_entry = (
    "- 2026-09-07: bench 第163回。16:37 JST tick。HEAD 4bb63d4 = bench 第162回 "
    "(16:25, K-Z3 16時台 run371 n-add cold 8/60) = remote net-kotobase/main 一致 "
    "(git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため "
    "git pull --ff-only 不可, fetch 系で取込; terminal foreground 出力不可=既知のため"
    "状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run "
    "計測)。host load1 36.45 (16:37 pre-run uptime 実測, gate 7.5 大幅超過) のため "
    "local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
    "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回"
    "帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第159回/"
    "bench 第162回「K-Z3 16hr n-add 続行, 次 run ID は run372 使用」) の run372 枠を"
    "本 tick 実施 (16時台 5 セット目, 前 tick bench 第162回 run371 済みの積み増し継続)。"
    "K-Z3 16時台 run372A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, "
    "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "16:36–16:40 JST, 全 80/80 200, secret 不含 — curl のみ): "
    "cold(>=0.5s) 0/0/1 per 20 = 1/60 (~1.7%) — run372A cold 0/20 p50 55.2ms / "
    "run372B cold 0/20 p50 47.6ms / run372C cold 1/20 (2.0526s 末尾単発) p50 46.2ms, "
    "control (kotobase.net/signup) cold 0/20 p50 43.8ms 完全静穏で control 分離成立。"
    "run371 8/60 → 本 tick 1/60 の散発減弱継続 (帯内 1 窓即消失型)。16時台 (9/7) 通算 "
    "= 21/300 (~7.0%) 5 セット高位帯候補。status 判定は rank に委ねる (rank 専門)。"
    "secret は一切記録せず。詳細は K-Z3 evidence 欄追記。NEXT: 委ねる (rank 指定優先; "
    "フォールバックは K-Z3 現在時刻帯 16時台 n 積み増し続行、次 run ID は run373 使用)"
)
# anchor: the falsify169 line that follows bench 第162回 in the iter log
anchor2 = "\n- 2026-09-07: falsify169: K-Z3 16hr(9/7) 2nd-set n-add run369 "
assert content.count(anchor2) == 1, f"anchor2 count={content.count(anchor2)}"
content = content.replace(anchor2, "\n" + iter_entry + anchor2, 1)

with io.open(F, "w", encoding="utf-8") as fh:
    fh.write(content)
print("INSERTED OK")