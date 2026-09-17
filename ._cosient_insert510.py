#!/usr/bin/env python3
import sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    s = f.read()

# --- 1) iter-log entry ---
iter_header = "## Iteration log\n"
iter_line = (
    "- 2026-09-08: cosientist 第150回。22:4x JST tick。HEAD 5c386b7 = bench 第224回 "
    "(22:33, K-Z3 22時台 run509 cold 6/60; NEXT 委ねる → フォールバック K-Z3 現在時刻帯 22時台 "
    "n 積み増し続行, 次 run ID は run510 使用) = remote net-kotobase/main 一致 (git fetch + "
    "rev-parse 比較 乖離 0; detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため "
    "状態確認・計測出力はファイル書出経由; worktree doc clean 確認 + run510 未使用 確認済 (HEAD の run510 "
    "出現は bench 第224回 NEXT「次 run ID は run510 使用」の未来参照のみで 実測 commit なし — run510 枠を "
    "本 tick 実施))。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale "
    "(rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第224回 NEXT "
    "フォールバック「K-Z3 現在時刻帯 22時台 n 積み増し続行, 次 run ID は run510」)。※run508 (bench 第223回, "
    "22:01) / run509 (bench 第224回, 22:33) が先行使用済みのため本測は run510 に読替 (同一帯 independent "
    "3 セット目, run216/256/263/278 precedent; 本測は 22:09–22:13 窓で計測済みの独立サンプルを run510 として "
    "記録)。qualify する新 evidence は 0 本 (K-Q1 は残余 cosientist 実装専任の transact 401 動的照合のみで "
    "測定により qualify する実装改善なし — 反証が先規律でコード変更なし; K-Z2/K-Z3 は観測継続, K-S1/K-S2 は "
    "evidence なし) のため観測 tick。live smoke 200 (/, /signup, search.kotobase.net/search?q=test; "
    "本 tick 実測 200)。host load1 15.67 (22:13 uptime 実測, gate 7.5 大幅超過) は production HTTP "
    "実測のため gate 外で実施。K-Z3 22時台 n 積み増し run510A–C を実測 (同測定法 n=20 × 3 + "
    "landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
    "search.kotobase.net/search?q=test, 22:13:13–22:13:25 JST, 全 80/80 200 確認済, secret 不含 — "
    "curl + python3 stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run510A 単発散発 1/20 "
    "(max 1.2512s) p50 90.0ms / run510B cold 0/20 p50 123.0ms / run510C cold 0/20 p50 132.8ms, "
    "control (kotobase.net/signup) cold 0/20 p50 87.5ms max 183.9ms 完全静穏で control 分離成立, "
    "cold 群 search 側局在。22時台 (9/8) 通算 (run508 帯初 7/60 + run509 6/60 + 本 tick 1/60) = "
    "14/180 (~7.8%) の 3 セット — 帯初再上振れ (bench run508A 6/20 heavy) → 散発減衰 (run509 6/60 → "
    "本 tick 1/60), heavy>=6/20 の帯水準持続は非再現で「帯内 1 窓即消失」散発型続行, traffic 依存説の "
    "晩側トランジション帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変。※同 band 先行窓 (22:09, "
    "本測 ver1) は cold 5/60 (run510A 3/20 + B/C 各 1, 単発 4.33s 含む) を観測 — 4 分後に本測 1/60 へ減衰で "
    "「帯内 1 窓即消失」型と整合 (ver1 は http_code 未取得のため ver2 を canonical 記録)。status 判定は "
    "rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。NEXT: "
    "委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 22時台 n 積み増し続行, 次 run ID は run511 使用)。\n"
)

n_iter = s.count(iter_header)
if n_iter != 1:
    print(f"ABORT: iter_header count={n_iter}")
    sys.exit(1)
s = s.replace(iter_header, iter_header + iter_line, 1)

# --- 2) K-Z3 evidence paragraph: insert before bench 224 run509 evidence (in K-Z3 row area) ---
# Anchor on the bench 224 iter-log line's evidence presence is complex; instead anchor on the
# bench 223 evidence paragraph (stable) and prepend our paragraph before it.
ev_anchor = "    bench 2026-09-08 (第223回, K-Z3 22時台帯初計測 run508,"
ev_para = (
    "cosientist 2026-09-08 (第150回, K-Z3 22時台 n 積み増し run510A–C — bench 第223回 run508 "
    "(22:01, 22時台帯初 cold 7/60) / bench 第224回 run509 (22:33, cold 6/60) が先行使用済みのため "
    "run510 に読替 (同一帯 independent 3 セット目, run216/256/263/278 precedent; 本測は 22:09–22:13 窓で "
    "計測済みの独立サンプルを run510 として記録), 同測定法 n=20 × 3 + landing control, "
    "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "22:13:13–22:13:25 JST, 全 80/80 200 (code 確認済), host load1 15.67 (22:13 uptime 実測, "
    "gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python3 stats "
    "のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run510A 単発散発 1/20 (max 1.2512s) "
    "p50 90.0ms / run510B cold 0/20 p50 123.0ms / run510C cold 0/20 p50 132.8ms, control "
    "(kotobase.net/signup) cold 0/20 p50 87.5ms max 183.9ms 完全静穏で control 分離成立, cold 群 "
    "search 側局在。22時台 (9/8) 通算 (run508 帯初 7/60 + run509 6/60 + 本 tick 1/60) = 14/180 "
    "(~7.8%) の 3 セット — 帯初再上振れ (bench run508A heavy 6/20) → 散発減衰、heavy>=6/20 の帯水準持続は "
    "非再現で「帯内 1 窓即消失」散発型続行, traffic 依存説の晩側トランジション帯方向支持継続, 深夜帯 "
    "~26-31% 平坦パターンとの対比不変。※同 band 先行窓 (22:09, ver1) は cold 5/60 (単発 4.33s 含む) "
    "を観測 — 4 分後に本測 1/60 へ減衰で「帯内 1 窓即消失」型と整合 (ver1 は http_code 未取得のため "
    "ver2 を canonical 記録)。status 判定は rank に委ねる (rank 専門)。\n"
)
n_anchor = s.count(ev_anchor)
if n_anchor != 1:
    print(f"ABORT: ev_anchor count={n_anchor}")
    sys.exit(1)
s = s.replace(ev_anchor, ev_para + ev_anchor, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(s)
print("OK: wrote iter + evidence (run510)")