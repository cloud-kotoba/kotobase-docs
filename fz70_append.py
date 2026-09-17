#!/usr/bin/env python3
# falsify 第70回 evidence append (K-Z3 行 evidence 欄末尾 + iteration log 末尾)
import io, sys

DOC = "query-cosientist.md"
NEW_EV = " falsify 2026-09-06 (K-Z3 6時台 3セット目 n 積み増し run188A–C, bench 第69回 run187A–C 直後の追加 n, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 06:33 JST, 全 80/80 200, host load1 ~130 (前 tick から急上昇, production HTTP 実測のため gate 外)): run188A cold(>=0.5s) 1/20 (0.971s 単発) p50 0.174s / run188B cold 0/20 p50 0.075s / run188C cold 0/20 p50 0.077s — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.143s (max 0.321s, 概ね静穏) で cold 分離成立だが control p50 も上振れ気味のため host load 高騰の混入可能性あり (borderline not-separated 傾向, 帯発現率採用可否は rank 判定に委ねる)。6時台は run186A 群発 (9/20, 06:16) → run187 0/60 (06:19) → run188 1/60 単発 (06:33) で群発窓は 2 tick 連続非再現 — 帯内 1 窓即消失型パターンを支持。status 判定は rank に委ねる (rank 専門)。"
LOG = "\n- 2026-09-06: falsify 第70回。06:31 JST tick。worktree detached HEAD のため fetch net-kotobase + checkout net-kotobase/main で取り込み (HEAD 85ec4c9 = fetch 後 main 先端一致)。falsify 第69回 (bfdfd7e, run186A-C) と bench 第69回 (85ec4c9, run187A-C) を取込み済み確認。host load1 ~130 (gate 7.5 超過, 直前 tick から急上昇) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 6時台 3セット目 run188A–C (同測定法 n=20 × 3 + landing control, 06:33 JST, 全 80/80 200): cold 1/0/0 per 20 = 1/60 (0.971s 単発, A のみ), warm p50 75–174ms, control cold 0/20 p50 143ms で概ね分離成立だが control 上振れ気味で borderline not-separated 傾向 — host load 高騰の混入可能性を注記。run186A 群発 (9/20) は 2 tick 連続非再現 (帯内 1 窓即消失型を支持)。status 遷移なし (rank 専門)。secret は一切記録せず鍵は zero-fill 該当なし (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 6時台 n 積み増し継続)。\n"

with io.open(DOC, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

hit = 0
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        hit += 1
        s = ln.rstrip()
        if s.endswith("|"):
            s = s[:-1].rstrip()
        lines[i] = s + NEW_EV + " |"
if hit != 1:
    sys.stderr.write("K-Z3 row match count = %d, abort\n" % hit)
    sys.exit(1)

text = "\n".join(lines)
with io.open(DOC, "w", encoding="utf-8") as f:
    f.write(text)

with io.open(DOC, "a", encoding="utf-8") as f:
    f.write(LOG)
print("appended ok, K-Z3 rows:", hit)
