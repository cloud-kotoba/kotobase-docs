#!/usr/bin/env python3
# Append falsify run507 evidence to END of K-Z3 row (line 279) of query-cosientist.md
import io, sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

assert len(lines) >= 279, "file too short"
ln = lines[279 - 1]  # 0-indexed -> line 279

# sanity: row is the K-Z3 hypothesis row and ends with rank delegation suffix
assert "| K-Z3 |" in ln, "line 279 is not K-Z3 row: %s" % ln[:60]
assert "rank 専門))" in ln or "rank 専門)" in ln, "unexpected line-279 tail"
assert not ln.rstrip().endswith("falsify 2026-09-08 (第225回"), "already appended"

EVID = (" falsify 2026-09-08 (第225回, K-Z3 21時台 n 積み増し run507A-C - 4 セット目, "
        "同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
        "正 endpoint search.kotobase.net/search?q=test, 21:51:10-21:51:27 JST, 全 80/80 200, "
        "host load1 35.89 (21:51 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため "
        "gate 外, secret 不含 - curl + python stats のみ): cold(>=0.5s) 3/1/0 per 20 = 4/60 "
        "(~6.7%) - run507A 冒頭隣接クラスタ 3/20 (pos2 1.2281s / pos3 1.1090s / pos5 1.6492s) "
        "p50 128.0ms / run507B 単発 1/20 (pos12 1.1857s) p50 99.1ms / run507C 0/20 p50 82.1ms, "
        "control (kotobase.net/signup) cold 0/20 p50 100.1ms max 166.2ms 完全静穏で control 分離成立, "
        "cold 群 search 側局在。21時台 (9/8) 通算 = run504 (9/60) + run505 (9/60) + run506 (4/60) "
        "+ run507 (4/60) = 26/240 (~10.8%) 4 セット - 晩側トランジション帯の帯初 heavy (run504A 8/20) "
        "以降の散発減衰続行 (run506 4/60 + 本 tick 4/60, heavy>=6/20 の帯水準持続非再現), cold 4 件 "
        "1.109-1.649s 閾値決定的。status 判定は rank に委ねる (rank 専門)。")

new_ln = ln.rstrip("\n") + EVID + "\n"
lines[279 - 1] = new_ln

with io.open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)

# verify occurrence count
with io.open(PATH, "r", encoding="utf-8") as f:
    txt = f.read()
cnt = txt.count("falsify 2026-09-08 (第225回")
sys.stdout.write("occurrences_225=%d\n" % cnt)
sys.stdout.write("line279_len_before=%d after=%d\n" % (len(ln), len(new_ln)))