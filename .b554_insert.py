#!/usr/bin/env python3
# falsify: insert run554 evidence (K-Z3 row END append) + iteration log line at top
import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")

ev = ("  falsify 第246回 run554 (11:32 JST, 11時台 5セット目, 同測定法 n=20 x3 + landing control, 別接続 curl, 全 60+20 測定, TTFB-only): "
      "cold(>=0.5s) 1/60 (~1.7%) - run554A 1/20 (1.4336s 単発) p50 73.7ms / run554B 0/20 p50 48.9ms / run554C 0/20 p50 51.3ms, "
      "control (kotobase.net/signup) 0/20 p50 42.2ms 完全静穏で分離成立。11時台通算 6/300 (~2.0%) 5セット - 低位帯一貫。"
      "run553 は bench 第253回 NEXT 予約のため本セットは run554 採番。2026-09-09")

iter = ("- 2026-09-09: falsify 第246回 (11:33 JST tick)。HEAD 06f19af = fetch 後 net-kotobase/main 一致 (乖離 0)。"
        "rank 第245回 NEXT「K-Z3 12hr帯初 run552」は bench 第253回 (11:25) が run552 を 11hr 4セット目として消化済みのため、"
        "本 tick は現 11時台 5セット目 run554A-C を実施 (run553 は bench NEXT 予約のため空番回避で run554 採番, 同測定法 n=20 x 3 + landing control, "
        "別接続 curl, Tokyo, 11:32 JST, 全 80 測定 TTFB-only): cold(>=0.5s) 1/60 (~1.7%) - run554A 1/20 (1.4336s 単発) p50 73.7ms / "
        "run554B 0/20 p50 48.9ms / run554C 0/20 p50 51.3ms, control 0/20 p50 42.2ms 完全静穏で control 分離成立。"
        "11時台通算 6/300 (~2.0%) 5セット。host load1 39.77 (gate 7.5 超過) は production HTTP 実測のため gate 外。"
        "evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる。K-Q1 (cacao_b64 harness 変更) は host load gate 超過のため本 tick も見送り。"
        "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 12時台帯初 n 積み増し)。secret は一切記録せず (curl + python3 stats のみ)。\n")

# locate K-Z3 evidence row
idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx = i
        break
assert idx is not None, "K-Z3 row not found"
row = lines[idx].rstrip()
if row.endswith("|"):
    row = row[:-1].rstrip()
lines[idx] = row + ev

# locate iteration log
it = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        it = i + 1
        break
assert it is not None, "iter log not found"
if not lines[it].startswith("- 2026"):
    it += 1
assert lines[it].startswith("- 2026"), "iter top not a log entry: " + lines[it][:40]
lines.insert(it, iter)

out = "\n".join(lines)
out = "".join(c for c in out if not (0x0300 <= ord(c) <= 0x036F))
with io.open(path, "w", encoding="utf-8") as f:
    f.write(out)
print("kz3_row", idx, "iter_at", it)
print("run554 count:", out.count("run554"))
print("falsify246 count:", out.count("falsify 第246回"))
