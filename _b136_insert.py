# -*- coding: utf-8 -*-
path = 'query-cosientist.md'
data = open(path, 'rb').read().decode('utf-8')

# 1) append measurement to K-Z3 evidence line (line 279, 1-indexed)
lines = data.split('\n')
kz3 = lines[278]  # line 279
assert kz3.startswith('| K-Z3 |'), "K-Z3 line anchor mismatch: %s" % kz3[:40]

evid = (
    " bench 2026-09-07 (第136回, K-Z3 7時台 n 積み増し run323A–C, 同測定法 n=20 × 3 + landing control, "
    "別接続 curl, cold>=0.5s TTFB, nearest-rank p50, Tokyo, 07:24:51–07:25:33 JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test, host load1 105.05 (07:22 uptime, gate 7.5 大幅超過) は "
    "production HTTP 実測のため gate 外): A cold 1/20 (0.9511s 単発) p50 59.2ms / B 0/20 p50 56.5ms / "
    "C 0/20 p50 57.5ms / CTRL 0/20 p50 54.0ms max 147.0ms — search cold 1/60 (~1.7%) 低位帯, "
    "control 完全静穏で control 分離成立, cold 群 search 局在, heavy run271A 型非再現 (49 セット), "
    "traffic-independence counter-evidence 継続。7時台通算 ≈12/420 (~2.9%)。status 判定は rank に委ねる "
    "(rank 専門)。secret は一切記録せず。"
)
lines[278] = kz3 + evid

# 2) insert new iteration-log entry just below "## Iteration log" (newest-first)
hdr = "## Iteration log"
idx = -1
for i, ln in enumerate(lines):
    if ln.rstrip() == hdr:
        idx = i
        break
assert idx != -1, "Iteration log header not found"

entry = (
    "- 2026-09-07: bench 第136回。07:23 JST tick。HEAD b08c6e4 = falsify 第149回 "
    "(07:18, 7時台 independent run322-indep cold 2/60) = remote net-kotobase/main 一致 "
    "(fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。"
    "live smoke 200 (/, /signup; pre-run 計測)。host load1 105.05 (07:22 uptime, gate 7.5 大幅超過) のため "
    "local 測定は拒否し production HTTP フォールバック (gate 外)。"
    "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (前帯 artifact) — "
    "true progressive NEXT は rank 第142回 commit「K-Z3 current-band(7hr) n-add run322」だが "
    "bench 第134回が run322 を先行使用済み (07:11) かつ falsify 第149回が independent run322-indep "
    "を実施済みで run322 ID は消費済み、本 tick は次 run ID run323 で 7時台帯 n 積み増しとして実施。"
    "K-Z3 7時台 n 積み増し run323A–C を本 tick 実測 (n=20×3 + landing control, 別接続 curl, cold>=0.5s, "
    "nearest-rank p50): A cold 1/20 (0.9511s 単発) p50 59.2ms / B 0/20 p50 56.5ms / C 0/20 p50 57.5ms / "
    "CTRL 0/20 p50 54.0ms max 147.0ms — search cold 1/60 (~1.7%) 低位帯, control 完全静穏で control 分離成立, "
    "cold 群 search 局在, heavy run271A 型非再現 (49 セット)。7時台通算 ≈12/420 (~2.9%)。"
    "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"
)
lines.insert(idx + 1, entry)

open(path, 'w').write('\n'.join(lines))
print("done, new line count:", len(lines))
print("verif line279 tail:", lines[278][-160:])
print("verif iterlog top:", lines[idx], "|", lines[idx+1][:60])