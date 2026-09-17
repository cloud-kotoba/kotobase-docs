import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

stem = (" cosientist 第143回 run476 (15:26 JST): cold>=0.5s 4/1/0 per20 = 5/60 (~8.3%) — "
"run476A 散発クラスタ 4/20 (1.0326s/1.2931s/1.2961s/1.516s) p50 60ms / run476B 単発 1/20 (1.2446s) / "
"run476C 0/20, control (kotobase.net/signup) 0/20 complete-quiet 分離成立, cold 群 search 側局在, "
"「帯内 1 窓即消失」散発型継続 (run475A heavy 6/20 の 9 分後減弱, heavy 帯水準は 2 セットで未確認)。"
"15時台 (9/8) 通算 = bench run475 (7/60 帯初) + run476 (5/60) = 12/120 (~10%) 中〜高位帯候補。"
"status 判定は rank に委ねる (rank 専門)。")

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")
idx = 278  # line 279 (0-based 278)
ln = lines[idx]
if not ln.startswith("| K-Z3 |"):
    raise SystemExit("line279 is not K-Z3 row: " + ln[:40])

lines[idx] = ln + stem

with io.open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("OK line279 appended, newlen", len(lines[idx]))