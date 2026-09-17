#!/usr/bin/env python3
# Append bench run503 K-Z3 evidence + iter-log entry. UTF-8, string anchors.
import io

DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

EVIDENCE = (
    " bench 2026-09-08 (第220回, K-Z3 20時台 n 積み増し run503A–C — falsify 第223回 run502 済の続行枠 "
    "(iter-log HEAD falsify 第223回 NEXT 委ねる → フォールバック K-Z3 現在時刻帯 20時台 n 積み増し, 次 run ID run503), "
    "同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
    "正 endpoint search.kotobase.net/search?q=test, 20:54:03–20:54:15 JST, 全 80/80 200, "
    "host load1 27.88 (20:53 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
    "secret 不含 — curl + python stats のみ): cold(>=0.5s) 2/1/0 per 20 = 3/60 (~5.0%) — "
    "run503A 散発 2/20 (pos4 2.2062s / pos12 1.1551s) p50 76.0ms max 2206.2ms / "
    "run503B 単発 1/20 (pos18 1.0397s) p50 49.0ms / run503C cold 0/20 p50 54.9ms max 151.0ms, "
    "control (kotobase.net/signup) cold 0/20 p50 48.7ms max 294.0ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
    "run503A/B 各散発単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 "
    "(run502A/B 各単発 (20:48) の ~6 分後, heavy>=6/20 非再現)。"
    "20時台 (9/8) 通算 = bench run499 (0/60, 帯初) + falsify run500 (6/60) + bench run501 (4/60) "
    "+ falsify run502 (2/60) + 本 tick run503 (3/60) = 15/300 (~5.0%) の 5 セット "
    "— 19時台 (9/240 ~3.8%) と同水準の晩側トランジション帯候補, 日中帯 (16-18時台 ~8.3-11.7%) より低位, "
    "traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変。"
    "帯 n=5 セットで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
)

ITER_ENTRY = (
    "- 2026-09-08: bench 第220回。20:54 JST tick。HEAD d61aa3a = falsify 第223回 (20:46, K-Z3 20時台 run502 cold 2/60 ~3.3%; "
    "NEXT 委ねる → 次 run ID run503) = remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系取込, "
    "terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書出経由; worktree doc clean + 挿入前 run503 未使用確認済 "
    "(HEAD d61aa3a の run503 出現は falsify 第223回 NEXT「次 run ID は run503 使用」の未来参照のみで実測 commit なし — run503 枠を本 tick 実施))。"
    "pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — "
    "true progressive NEXT は iter-log HEAD 連鎖 (falsify 第223回 NEXT 委ねる → フォールバック K-Z3 現在時刻帯 20時台 n 積み増し, 次 run ID run503)。"
    "host load1 27.88 (20:53 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。"
    "live smoke 200 (/, /signup, search.kotobase.net/search?q=test; 本 tick 実測 200)。"
    "K-Z3 20時台 n 積み増し run503A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, "
    "nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:54:03–20:54:15 JST, 全 80/80 200, "
    "secret 不含 — curl + python stats のみ): cold(>=0.5s) 2/1/0 per 20 = 3/60 (~5.0%) — "
    "run503A 散発 2/20 (pos4 2.2062s / pos12 1.1551s) p50 76.0ms max 2206.2ms / "
    "run503B 単発 1/20 (pos18 1.0397s) p50 49.0ms / run503C 0/20 p50 54.9ms, "
    "control (kotobase.net/signup) 0/20 p50 48.7ms max 294.0ms 完全静穏で control 分離成立, cold 群 search 側局在。"
    "run503A/B 各散発単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」型継続 (run502 (20:48) の ~6 分後, heavy>=6/20 非再現)。"
    "20時台 (9/8) 通算 = run499 (0/60) + run500 (6/60) + run501 (4/60) + run502 (2/60) + run503 (3/60) = 15/300 (~5.0%) 5 セット — "
    "19時台 (9/240 ~3.8%) と同水準の晩側トランジション帯候補, traffic 依存説の日中帯方向支持継続, "
    "深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。"
    "詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行, 次 run ID は run504 使用)。"
)

with io.open(DOC, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1) Append evidence to K-Z3 hypothesis row (line starting with "| K-Z3 |")
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.lstrip().startswith("| K-Z3 |"):
        kz3_idx = i
        break
assert kz3_idx is not None, "K-Z3 row not found"
lines[kz3_idx] = lines[kz3_idx].rstrip("\n") + EVIDENCE + "\n"

# 2) Insert iter-log entry right after "## Iteration log" header line
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == "## Iteration log":
        hdr_idx = i
        break
assert hdr_idx is not None, "Iteration log header not found"
lines.insert(hdr_idx + 1, ITER_ENTRY + "\n")

with io.open(DOC, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("OK: K-Z3 row line=%d, iter-log header line=%d" % (kz3_idx + 1, hdr_idx + 1))