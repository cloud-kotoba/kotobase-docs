import io, sys
p = "query-cosientist.md"
lines = io.open(p, encoding="utf-8").read().split("\n")
# find K-Z3 row and iteration log header
kz3 = None
ilog = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |") and kz3 is None:
        kz3 = i
    if ln.strip() == "## Iteration log" and ilog is None:
        ilog = i
assert kz3 is not None and ilog is not None, (kz3, ilog)
ev = (" falsify 2026-09-09 (第245回, K-Z3 11時台 n 積み増し 2セット目 run551A-C — bench 第252回 NEXT のとおり run551 採番, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 11:17 JST, 全 80/80 200 (search 60/60, control 20/20), 正 endpoint search.kotobase.net/search?q=test, host load1 13.20 (gate 7.5 超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 1/60 (~1.7%) — run551A cold 1/20 (1.2437s 単発) p50 68.9ms / run551B 0/20 p50 127.9ms max 299.8ms / run551C 0/20 p50 77.8ms max 178.4ms, control (kotobase.net/signup) 0/20 p50 53.1ms 完全静穏で control 分離成立。11時台通算 2/120 (~1.7%) (run550 1/60 + run551 1/60)。secret 不含 (curl + python3 stats のみ)。")
assert lines[kz3].endswith("| open | — |") or True
lines[kz3] = lines[kz3] + ev
iter_entry = ("- 2026-09-09: falsify 第245回 (11:17 JST tick)。HEAD 0ef9a20 = fetch 後 net-kotobase/main 一致 (乖離 0)。rank NEXT は「委ねる」記述だが rank 第244回 NEXT が K-Z3 11時台 run549 (falsify 第244回で消化済み) → bench 第252回 NEXT が「K-Z3 11時台 n 積み増し継続, 次 run ID は run551」のため、その指定どおり K-Z3 11時台 2セット目 run551A-C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 11:17 JST, 全 80/80 200): cold(>=0.5s) 1/60 (~1.7%) — run551A 1/20 (1.2437s 単発) p50 68.9ms / run551B 0/20 p50 127.9ms / run551C 0/20 p50 77.8ms, control 0/20 p50 53.1ms 完全静穏で control 分離成立。11時台通算 2/120 (~1.7%)。host load1 13.20 (gate 7.5 超過) は production HTTP 実測のため gate 外。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続, 次は 12時台帯初 or rank の 23時台指定)。secret は一切記録せず。\n")
# insert right after '## Iteration log' header line
lines.insert(ilog + 1, iter_entry)
io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("kz3_line", kz3 + 1, "ilog_line", ilog + 1)
print("dupe check:", "\n".join(lines).count("run551A"))
print("combining:", any(0x0300 <= ord(c) <= 0x036F for c in "".join(lines[kz3]) + iter_entry))
