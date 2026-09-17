# -*- coding: utf-8 -*-
import sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(PATH, encoding="utf-8").read().replace("\r\n", "\n")
lines = s.split("\n")

if "cosientist 2026-09-08 (第144回, K-Z3 16時台 n 積み増し run482A" in s:
    print("ALREADY_PRESENT cosientist-144 run482; abort without edit")
    sys.exit(0)

il = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        il = i
        break
assert il is not None, "Iteration log header not found"
last_ev_idx = il - 1

ev_rec = (
    "cosientist 2026-09-08 (第144回, K-Z3 16時台 n 積み増し run482A–C — bench 第209回 NEXT 委ねる "
    "のフォールバック「K-Z3 現在時刻帯 16時台 n 積み増し続行, 次 run ID run482」, 同測定法 n=20 × 3 "
    "+ landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net"
    "/search?q=test, 16:44–16:45 JST, 全 80/80 200, host load1 63.89 (16:45 uptime 実測, "
    "gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats "
    "のみ): cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10.0%) — run482A 散発クラスタ 5/20 "
    "(0.5708s/0.6348s/1.1386s/1.1797s/1.7909s) p50 145.7ms / run482B 単発 1/20 (1.2504s) "
    "p50 82.7ms / run482C cold 0/20 p50 151.9ms, control (kotobase.net/signup) "
    "cold 0/20 p50 74.8ms max 471.7ms 完全静穏で control 分離成立, cold 群 search 側局在。"
    "run482A 散発 5/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ型継続 "
    "(run479A 5/20 (16:06) の ~38 分後再上振れ, heavy>=6/20 は 16時台で未達)。"
    "16時台 (9/8) 通算 = run479 6/60 (帯初) + run480 5/60 + run481 3/60 + 本 tick run482 6/60 "
    "= 20/240 (~8.3%) の 4 セット中〜高位帯 — 帯初再上振れ (6/60) → 帯内散発減衰 (5/60 → 3/60) "
    "→ 再上振れ (6/60) の日中帯 high 側パターン継続、traffic 依存説の日中帯方向支持継続、"
    "深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。"
)
lines[last_ev_idx] = lines[last_ev_idx] + "\n" + ev_rec

ilog_rec = (
    "- 2026-09-08: cosientist 第144回。16:44 JST tick。HEAD 9807184 = bench 第209回 "
    "(16:35, K-Z3 16時台 run481 cold 3/60) = remote net-kotobase/main 一致 (detached HEAD のため "
    "fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; "
    "pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回 "
    "artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第209回 NEXT 委ねる → フォール"
    "バック K-Z3 現在時刻帯 16時台 n 積み増し, 次 run ID run482))。qualify する新 evidence は 0 本 "
    "(K-Q1 は残余 cosientist 実装専任の動的照合のみ・測定で qualify する実装なし (反証が先規律), "
    "K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし) — コード変更なし。live smoke 200 (/, /signup; "
    "pre-run + 本 tick 実測 200)。host load1 63.89 (16:45 uptime 実測, gate 7.5 大幅超過) は production "
    "HTTP 実測のため gate 外で K-Z3 観測を実施。K-Z3 16時台 run482A–C を実測 (同測定法 n=20 × 3 "
    "+ landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
    "search.kotobase.net/search?q=test, 16:44–16:45 JST, 全 80/80 200, secret 不含 — curl + python "
    "stats のみ): cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10.0%), control 0/20 完全静穏分離成立。"
    "16時台 (9/8) 通算 = run479 6/60 + run480 5/60 + run481 3/60 + 本 tick run482 6/60 "
    "= 20/240 (~8.3%) の 4 セット中〜高位帯。status 判定は rank 専門。secret 不含。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 16時台 n 積み増し続行, 次 run ID は run483)。"
)
lines.insert(il + 1, ilog_rec)

open(PATH, "w", encoding="utf-8").write("\n".join(lines))
print("INSERTED run482 evidence + iter-log entry")