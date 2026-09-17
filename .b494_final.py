# -*- coding: utf-8 -*-
# falsify 第220回: append run494 evidence to K-Z3 row + insert iter-log
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# --- 1) append evidence to K-Z3 row (physical line starting with "| K-Z3 |") ---
ki = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        ki = i
        break
assert ki is not None, "K-Z3 row not found"

ev = (
" falsify 2026-09-08 (第220回, K-Z3 18時台 run494A-C（bench 第215回 run493 と同時刻帯の独立実測, "
"run ID 衝突のため run494 に読替）, 同測定法 n=20 × 3 + landing control, 別接続 curl, "
"cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test + control kotobase.net/signup, "
"18:46–18:47 JST, 全 80/80 200, host load1 140.36 (18:46 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
"secret 不含 — curl のみ): cold(>=0.5s) 7/1/0 per 20 = 8/60 (~13.3%) — "
"run494A 散発クラスタ 7/20 (0.6425/0.6952/1.1261/1.1327/1.1588/1.3149/1.6510s) p50(rank10) 0.203s max 1.651s / "
"run494B 単発 1/20 (0.9664s) p50 0.062s / run494C 0/20 p50 0.098s "
"— landing control (kotobase.net/signup) cold 0/20 p50 0.095s max 0.305s 完全静穏で control 分離成立、cold 群は search 側に局在。"
"18時台 (9/8) 通算 = run489 (7/60) + run490 (7/60) + run491 (6/60) + run492 (4/60, bench) + run493 (3/60, bench 第215回) + 本測 run494 (8/60) = 35/360 (~9.7%) "
"の 6 セット日中帯高位継続, 17時台 (28/240 ~11.7%) と同水準で traffic 依存説の日中帯方向支持継続、"
"深夜帯 ~26–31% 平坦パターンとの対比不変。status 判定は rank 専門。 secret 不含。"
)

old = lines[ki]
assert "falsify 2026-09-08" not in old[-260:], "already appended this tick"
lines[ki] = old.rstrip("\n") + ev + "\n"

# --- 2) insert iter-log at top (right after "## Iteration log") ---
iter_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        iter_idx = i
        break
assert iter_idx is not None, "Iteration log header not found"

iter_entry = "- 2026-09-08: falsify 第220回。19:05 JST tick。HEAD 6c0a2a1 = bench 第215回 (18:56, K-Z3 18時台 run493 cold 3/60; NEXT 委ねる → run494) = remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル経由)。K-Z3 18時台 の独立実測を実施 (bench run493 と同時刻帯, 別接続 curl n=20 × 3 + landing control, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 18:46–18:47 JST 窓, 全 80/80 200): cold(>=0.5s) 7/1/0 per 20 = 8/60 (~13.3%) — run494A 散発クラスタ 7/20 (0.64–1.65s) / B 単発 1/20 (0.97s) / C 0/20, landing control 0/20 完全静穏で control 分離成立、cold 群 search 側局在。run ID 衝突のため run494 に読替 (bench 第215回 が同時刻帯 run493 を先行使用)。18時台 (9/8) 通算 = 35/360 (~9.7%) の 6 セット日中帯高位継続、17時台 (28/240 ~11.7%) と同水準で traffic 依存説の日中帯方向支持継続、深夜帯 ~26–31% 平坦パターンとの対比不変。status 判定は rank 専門。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run495)。\n"

lines.insert(iter_idx + 1, iter_entry)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

# verify
with open(path, "r", encoding="utf-8") as f:
    l2 = f.readlines()
kzi = None
for i, ln in enumerate(l2):
    if ln.startswith("| K-Z3 |"):
        kzi = i
        break
print("K-Z3 run493 count:", l2[kzi].count("run493"))
print("K-Z3 run494 count:", l2[kzi].count("run494"))
for i, ln in enumerate(l2):
    if ln.strip() == "## Iteration log":
        print("iter second line starts dash:", l2[i+1].startswith("-"))
        print("iter second line contains run494:", "run494" in l2[i+1])
        break
print("done")