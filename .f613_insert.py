import io, sys
p = "query-cosientist.md"
s = open(p, encoding="utf-8").read()

# --- 1) evidence append at END of K-Z3 row (line starting '| K-Z3 |', the one with 'bench 2026-09-13' evidence)
lines = s.split("\n")
kz3_idx = [i for i, l in enumerate(lines) if l.startswith("| K-Z3 |") and "bench 2026-09-13" in l]
assert len(kz3_idx) == 1, kz3_idx
i = kz3_idx[0]
assert lines[i].endswith("|"), lines[i][-40:]
ev = " falsify 2026-09-14 (第251回, K-Z3 7時台 (9/14) 帯初計測 run613A-C, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 07:44:23-07:44:40 JST, 全 80/80 200, host load1 12.25-14.37 (gate 7.5 超過) は production HTTP 実測のため gate 外): run613A cold(>=0.5s) 8/20 (831-1538ms クラスタ) p50 50.9ms / run613B cold 2/20 (1065.0/1250.0ms) p50 41.5ms / run613C cold 0/20 p50 41.9ms — cold(>=0.5s) 計 10/60 (~16.7%)。landing control (kotobase.net/signup) cold 1/20 (612.5ms 単発) p50 44.1ms で search 側クラスタは control 分離傾向だが control 単発 cold 1 件あり分離は弱い (leaning-separated)。9/6 7時台 run192+193+194 4/180 (~2.2%) と同帯日次ペアで 9/14 は 10/60 (~16.7%) — 同一帯で日差 ~7.6 倍の開きは K-Z4 (日次変動成分) の直接材料。status 判定は rank に委ねる。"
lines[i] = lines[i] + ev

s = "\n".join(lines)

# --- 2) iteration log entry right after '## Iteration log'
il = s.index("## Iteration log")
il_end = s.index("\n", il) + 1
entry = "- 2026-09-14: falsify 第251回 (07:40 JST tick)。HEAD 121700d = fetch 後 net-kotobase/main 先端一致 (detached HEAD; fetch + rev-parse 比較, 乖離 0)。monitor: host load1 15.40 (7:40 pre-run 実測, gate 7.5 超過 — production HTTP 実測なら gate 外), live smoke 200/200 (/, /signup; pre-run monitor 計測)。rank 第268回 NEXT「K-Z3 7時台 (9/14) 帯初計測 run613」に従い production HTTP 実測で run613A-C を実施 (同測定法 n=20 x3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, Tokyo, 07:44:23-07:44:40 JST, 全 80/80 200): cold 計 10/60 (~16.7%) — run613A 8/20 (831-1538ms クラスタ) p50 50.9ms / run613B 2/20 p50 41.5ms / run613C 0/20 p50 41.9ms, control (kotobase.net/signup) cold 1/20 (612.5ms 単発) p50 44.1ms で leaning-separated。9/6 同帯 4/180 (~2.2%) vs 9/14 10/60 (~16.7%) の日差 ~7.6 倍は K-Z4 日次変動成分の直接材料。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず (curl + python3 stats のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現時刻帯 n 積み増し継続, 次 run ID は run614 使用)。\n"
s = s[:il_end] + entry + s[il_end:]

open(p, "w", encoding="utf-8").write(s)
print("ok")
