#!/usr/bin/env python3
# Append falsify run312 evidence to K-Z3 hypothesis line (line index 278 = display 279).
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

# locate the K-Z3 hypothesis line
target = None
for i, ln in enumerate(lines):
    if "| K-Z3 |" in ln and "run194" in ln:
        target = i
        break
if target is None:
    raise SystemExit("K-Z3 line not found (run194 anchor)")

# sanity: assert known trailing text before appending
anchor = "band="
if anchor not in lines[target]:
    # fallback anchor
    anchor = "status 判定は rank に委ねる (rank 専門)"


ADDS = (
    " falsify 2026-09-07 (第143回, K-Z3 5時台(深夜帯) n 積み増し run312A-C - bench 第129回 run311 (05:17) に続く 5時台 n 積み増し (次 run ID run312), "
    "同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 05:31:44-05:32:06 JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test, host load1 25.80-25.88 (05:31/05:32 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
    "secret 不含 - curl のみ): cold(>=0.5s) 0/0/0/0 per 20 = 0/60 完全静穏 - run312A cold 0/20 p50 52.9ms max 131.3ms / "
    "run312B cold 0/20 p50 84.2ms max 145.1ms / run312C cold 0/20 p50 54.7ms max 100.9ms, "
    "control (kotobase.net/signup) cold 0/20 p50 57.5ms max 132.8ms 完全静穏で control 分離成立 (search/control とも 0 cold)。"
    "run312 全 0/60 完全静穏で 5時台の完全静穏 0/60 は run283/289/293/296/297/298/303/307/309 型の 10 例目 "
    "(run310 2/60 散発単発直後の再静穏 = 散発単発=即消失の性質を 10 例目で支持, heavy クラスタ run271A 6/20 型は run271A 以降 37 セット連続非再現)。"
    "5時台通算 run309 (0/60) + run310 (2/60) + run311 (1/60) + 本 tick run312 (0/60) = 3/240 (~1.25%) 4 セット、"
    "deep-night 累計 run275..312 = 40/2280 (~1.75%) 38 セットで低位帯水準継続 - 深夜帯 traffic 最低帯 (5時台) での完全静穏多発 "
    "(0/60 が run309 + run312 の 2/4 セット) は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
    "status 判定は rank に委ねる (rank 専門)。"
)

lines[target] = lines[target].rstrip("\n") + ADDS + "\n"

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

# verify single occurrence
with open(path, encoding="utf-8") as f:
    content = f.read()
cnt = content.count("run312A cold 0/20")
print(f"run312 evidence occurrence count = {cnt}")
with open("/tmp/fz312_insert_check.txt", "w", encoding="utf-8") as f:
    f.write(f"occurrence={cnt}\n")