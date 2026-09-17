# -*- coding: utf-8 -*-
# Insert run508 (bench 223) evidence into K-Z3 row + iter-log entry.
# Operates on a copy at /tmp/b508_edit.md; caller writes over working tree.
import io

SRC = "/tmp/b508_edit.md"
with io.open(SRC, "r", encoding="utf-8") as f:
    txt = f.read()
lines = txt.split("\n")

# --- 1) append evidence line before "## Iteration log" ---
iter_idx = None
for i, ln in enumerate(lines):
    if ln.rstrip().startswith("## Iteration log"):
        iter_idx = i
        break
assert iter_idx is not None, "iter log header not found"
# insertion point for evidence = iter_idx (insert before header)
evidence_line = (
    "    bench 2026-09-08 (第223回, K-Z3 22時台帯初計測 run508, 同測定法 n=20 × 3 + "
    "landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
    "search.kotobase.net/search?q=test, 22:01:06–22:01:32 JST, 全 80/80 200, "
    "host load1 ~45–54 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外): "
    "run508A heavy 散発クラスタ 6/20 (pos1,2,5,6,13,19: 4.139s/1.235s/1.538s/1.532s/"
    "2.366s/1.318s) + run508B 単発 1/20 (1.029s pos9) + run508C 0/20 → search cold "
    "7/60 (~11.7%), control 0/20 完全静穏で分離成立。22時台帯初 (9/8) は 21時台 "
    "(run504-507 26/240 ~10.8%) と同水準の中位帯 — 夜帯遷移として traffic 依存説方向を継続支持。"
)
lines.insert(iter_idx, evidence_line)
# now header moved +1; reindex
iter_idx = None
for i, ln in enumerate(lines):
    if ln.rstrip().startswith("## Iteration log"):
        iter_idx = i
        break
assert iter_idx is not None

# --- 2) insert iter-log entry after header ---
iterlog_line = (
    "- 2026-09-08: bench 第223回。22:01 JST tick。HEAD 1c22636 = falsify 第225回 "
    "(21:51, K-Z3 21時台 run507 cold 4/60 ~6.7%; NEXT 委ねる → run508) = remote "
    "net-kotobase/main 一致 (fetch + rev-parse 比較 乖離 0; detached HEAD のため fetch 系取込; "
    "terminal stdout 空=既知)。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale "
    "(rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖の「21時台 n 積み増し続行」⇒ "
    "21時台は run504-507 で 4 セット 26/240 ~10.8% 済みのため、本 tick は 実行時刻 22:01 の 22時台帯初計測へシフト。"
    "K-Z3 22時台帯初計測 run508 実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, "
    "search.kotobase.net/search?q=test, 22:01:06–22:01:32 JST, 全 80/80 200): search cold 7/60 "
    "(~11.7%; run508A heavy 散発クラスタ 6/20 pos1,2,5,6,13,19 + B 単発), control 0/20 完全静穏で分離成立。"
    "host load1 ~45–54 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外。evidence は K-Z3 仮説行に追記済み。"
    "secret は一切記録せず。"
)
lines.insert(iter_idx + 1, iterlog_line)

out = "\n".join(lines)
with io.open(SRC, "w", encoding="utf-8") as f:
    f.write(out)
# read-back verification
with io.open(SRC, "r", encoding="utf-8") as f:
    rt = f.read()
print("OK bytes_in=%d bytes_out=%d readback=%d run508_in_rt=%s" % (
    len(txt), len(out), len(rt), ("run508" in rt)))