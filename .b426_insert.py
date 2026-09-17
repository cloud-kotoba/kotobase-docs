# insert bench run426 evidence into K-Z3 row + iter-log entry
fn = 'query-cosientist.md'
text = open(fn, encoding='utf-8').read()
lines = text.split('\n')

evo = " bench 2026-09-08 (第189回, K-Z3 6時台 n 積み増し run426A–C — iter-log HEAD(falsify 第187回, 06:04, run425 帯初 0/60) の続行枠 run426, 同測定法 n=20 × 3 + landing control, 別接続 curl,cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 06:15–06:19 JST, 全 80/80 200, host load1 24.04 (06:22 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/1/0 per 20 =  ​2/60 (~3.3%) — run426A 単発散発 1/20 (1.52s) p50 43.2ms max 1520.1ms / run426B 単発 1/20 (0.969s) p50 43.1ms max 969.4ms / run426C cold 0/20 p50 43.9ms max 131.7ms, control (kotobase.net/signup) cold 0/20 p50 43.1ms max 126.2ms 完全静穏で control 分離成立, cold 群は search 側に局在。run426A/B 各単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (run425 帯初 0/60 完全静穏の直後の再出現, heavy>=6/20 は run413A 以降非再現継続)。6時台 (9/8) 通算 = falsify-run425 (0/60, 帯初) + 本 tick run426 (2/60) =  ​2/120 (~1.7%) の 2 セット低〜中位帯候補 — 朝帯境の歴朝低位帯 (9/5 6時台 2/300 ~0.67% / 9/7 6時台 7/420 ~1.67%) と同水準の低位帯継続, 深夜帯→朝帯境静穏方向に整合し K-Z3 traffic 依存説への強反証材料なし, 帯 n=2 セットのみで帯水準確定・機構判断には rank 追加 n を要する)。status 判定は rank に委ねる (rank 専門)。"

kz3_index = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        kz3_index = i
        break
if kz3_index is None:
    raise SystemExit('K-Z3 row not found')
lines[kz3_index] = lines[kz3_index] + evo.rstrip()

ilog = "- 2026-09-08: **bench 第189回**　06:22 JST tick、HEAD 348875d = rank  ​第186回 (06:18, fold falsify187-run425 -> 6時台帯初 0/60 完全静穏) = remote bench_fetch/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込)。live smoke 200 (/, /signup; pre-run 計測)。host load1 24.04 (06:22 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP​​ 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (rank 第186回, 06:18, run425 済)「K-Z3 6時台 n 積み増し継続 (次 run ID run426)」の run426 枠を本 tick 実施 (6時台 2セット目, falsify 第187回 run425 (06:04, 帯初 0/60) の続行)。K-Z3 6時台 run426A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl,cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 06:15–06:19 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/1/0 per  20 =  2/60 (~3.3%) — run426A 単発散発 1/20 (1.52s, p50 43.2ms, max 1520.1ms) / run426B 単発 1/20 (0.969s, p50 43.1ms, max 969.4ms) / run426C 0/20 p50 43.9ms max 131.7ms, control (kotobase.net/signup) cold 0/20 p50 43.1ms max 126.2ms 完全静穏で control 分離成立, cold 群 search 側局在, 「帯内 1 窓即消失」散発単発型継続 (run425 帯初 0/60 完全静穏の直後の再出現, heavy>=6/20 は run413A 以降非再現継続)。6時台 (9/8) 通算 = falsify-run425 (0/60, 帯初) + 本 tick 2/60 =  2/120 (~1.7%) の 2 セット低〜中位帯候補 — 朝帯境の歴朝低位帯 (9/5 6時台 2/300, 9/7 6時台 7/420 ~1.67%) と同水準の低位帯継続, 深夜帯→朝帯境静穏方向に整合し K-Z3 traffic 依存説への強反証材料なし, 帯 n=2 セットのみで帯水準確定・機構判断には rank 追加 n を要する)。qualify する新 evidence は 1 本 (K-Z3 run426) のため cosientist 実装対象なし — 観測 tick。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず.詳細は K-Z3 evidence 欄 (L279 末尾追記).NEXT: 委ねる (rank 指定優先,フォールバックは K-Z3 現在時刻帯 6時台 n 積み増し続行, 次 run ID は run427 使用)。"

hdr = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        hdr = i
        break
if hdr is None:
    raise SystemExit('iter log header not found')
lines.insert(hdr+1, ilog)

open(fn, 'w', encoding='utf-8').write('\n'.join(lines))
print('INSERT-OK kz3_index', kz3_index+1, 'hdr', hdr+1)