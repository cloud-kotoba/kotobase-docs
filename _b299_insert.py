import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as fh:
    text = fh.read()

# ---- Iteration log entry (newest-first: insert right after header) ----
iter_anchor = "## Iteration log\n"
assert text.count(iter_anchor) == 1, "iter header count=" + str(text.count(iter_anchor))

iter_entry = "- 2026-09-07: bench 第123回。03:54 JST tick。HEAD 58dd249 = falsify 第136回 (run298A-C, 03:47, 3時台 n-add, cold 0/60 完全静穏) = remote net-kotobase/main 一致 (fetch + rev-parse, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 41.05 (03:54 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。rank 第130回 NEXT「K-Z3 現時刻帯 3時台 n 積み増し継続」の現時刻帯フォールバック継続として 3時台 n 積み増し run299A–C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, 03:54:28–03:54:37 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run299A 単発 1.3222s p50 56.4ms / run299B 0/20 p50 47.4ms / run299C 0/20 p50 41.1ms, control (kotobase.net/signup) cold 0/20 p50 45.8ms max 79.0ms 完全静穏で control 分離成立、cold 群は search 側に局在。run299A 単発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (falsify run298 完全静穏 0/60 直後の再出現, heavy クラスタは run271A 以降 25 セット非再現)。3時台通算 (run291..299 = 8/540 ~1.5% 9-set)、deep-night 累計 run275..299 = 30/1500 (~2.0%) の 25 セットで低位帯水準続位 — 深夜最低帯 (traffic 最低) での cold 散発再出現は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run300 使用)。※pre-run monitor NEXT「深夜帯 23時台」は rank 第90回帯 stale スナップショット (rank 第114回で共有判断済み) — 真の NEXT は現時刻帯 3時台 n 積み増し継続。"

text = text.replace(iter_anchor, iter_anchor + iter_entry + "\n", 1)

# ---- K-Z3 evidence cell append (anchor on unique falsify136 cumulative tail) ----
kz_anchor = "deep-night 累計 run275..298 = 29/1440 (~2.0%) の 24 セットで低位帯水準続位"
assert text.count(kz_anchor) == 1, "kz anchor count=" + str(text.count(kz_anchor))

kz_evidence = (
    " bench 2026-09-07 (第123回, K-Z3 3時台(深夜帯) n 積み増し run299A–C — falsify 第136回 run298 (03:47) に続く 3時台 n 積み増し (次 run ID run299), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 03:54:28–03:54:37 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 41.05 (03:54 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run299A cold 単発 1.3222s p50 56.4ms / run299B cold 0/20 p50 47.4ms max 81.5ms / run299C cold 0/20 p50 41.1ms max 89.6ms, control (kotobase.net/signup) cold 0/20 p50 45.8ms max 79.0ms 完全静穏で control 分離成立、cold 群は search 側に局在。run299A 単発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (falsify run298 完全静穏 0/60 直後の再出現, heavy クラスタは run271A 6/20 以降 25 セット非再現)。3時台通算 (run291 2/60 + run292 1/60 + run293 0/60 + run294 2/60 + run295 2/60 + run296 0/60 + run297 0/60 + run298 0/60 + 本 tick 1/60) = 8/540 (~1.5%) の 9 セット、deep-night 累計 run275..299 = 30/1500 (~2.0%) の 25 セットで低位帯水準続位 — 深夜最低帯 (traffic 最低) での cold 散発再出現は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる (rank 専門)。"
)
text = text.replace(kz_anchor, kz_anchor + kz_evidence, 1)

with io.open(path, "w", encoding="utf-8") as fh:
    fh.write(text)

# verify
with io.open(path, "r", encoding="utf-8") as fh:
    check = fh.read()
print("iter inserted:", check.count(iter_entry) == 1)
print("kz inserted:", check.count("run299A cold 単発 1.3222s") == 1)
print("iter headline:", check.split("## Iteration log\n",1)[1].split("\n",1)[0][:40])