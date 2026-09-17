#!/usr/bin/env python3
lines=open('query-cosientist.md',encoding='utf-8').read().split('\n')

ADD_kz3 = " falsify 2026-09-07 (第150回, K-Z3 7時台 n 積み増し run324A–C (次 run ID, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 07:33:12–07:34:01 JST, host load1 146.51 (07:34 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ, 全 80/80 200): cold(>=0.5s) 3/2/1 per 20 = 6/60 (~10.0%) — run324A cold 3/20 (1.4719s / 1.1170s / 0.6407s 散発配置, warm p50 265ms) p50 265ms / run324B cold 2/20 (0.6160s / 0.5492s) p50 228ms / run324C cold 1/20 (0.5182s 境界値) p50 211ms, control (kotobase.net/signup) cold 2/20 (0.5909s / 0.5627s) p50 250ms — ※本 tick は host load1 146.51 の極端高負荷 tick で search/control とも p50 全体的上振れ (search 211–265ms, control 250ms vs 静穏基準 40–50ms) かつ control にも cold 2 件 (0.56/0.59s 境界値) が出現し control 分離は borderline not-separated 傾向 (search 側 cold 6/60 は素上 3 件 1.12–1.47s で閾値決定的だが control にも同規模 delayed が出たため機構判定としては弱い)。run324A 散発 3/20 + B 2/20 + C 1/20 は heavy run271A 型の弱い再上振れ (host-load 汚染込みで heavy 確定は不可) — 「帯内 1 窓即消失」散発単発/クラスタ型の弱連続で heavy (6/20 型) は run271A 以降 50 セット連続非再現のまま。7時台通算は rank 判定に委ねる (run321 3/60 + run322-indep 2/60 + run323 1/60 + 本 run324 6/60 not-separated の算入可否)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"

# append to K-Z3 row (index 278)
lines[278] = lines[278] + ADD_kz3

# iteration log header index (0-based)
ilog = 357  # '## Iteration log' at line 358 (1-based) -> idx 357
# find first '-' entry after it: insert newest at ilog+1
entry = "- 2026-09-07: falsify 第150回。07:34 JST tick。HEAD 3c72b7f = bench 第136回 (07:23, 7時台 run323 cold 1/60) = remote net-kotobase/main 一致 (fetch net-kotobase + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 119.69 (07:30 uptime) → 146.51 (07:34 測定時, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (前帯 artifact) — true progressive NEXT は rank 第142回 commit「K-Z3 current-band(7hr) n-add run322」だが run322 は falsify 第149回が independent 実施済み + bench 第134回使用済み、run323 も bench 第136回使用済みで本 tick は次 run ID run324 で 7時台帯 n 積み増しとして実施。K-Z3 7時台 n 積み増し run324A–C を本 tick 実測 (n=20×3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50): A cold 3/20 (1.4719/1.1170/0.6407s) p50 265ms / B cold 2/20 (0.6160/0.5492s) p50 228ms / C cold 1/20 (0.5182s 境界値) p50 211ms / CTRL cold 2/20 (0.5909/0.5627s) p50 250ms — search cold 6/60 (~10.0%) だが control にも cold 2 件 + 全 p50 上振れ (host load 146 極端高負荷 tick) で borderline not-separated, heavy run271A 型非再現 (50 セット)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"

lines.insert(ilog+1, entry)

open('query-cosientist.md','w',encoding='utf-8').write('\n'.join(lines))
print("done")