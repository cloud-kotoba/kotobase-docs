path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(path, encoding='utf-8') as fh:
    lines = fh.readlines()

ev = (" falsify 2026-09-14 (第250回, K-Z3 3時台帯初 run611A-C, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 03:42-03:44 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 9.49 (3:44 uptime) は production HTTP 実測のため gate 外): cold(>=0.5s) 9/1/1 per 20 = 11/60 (~18.3%) - run611A 散発クラスタ 9/20 (739-1406ms 群発, warm p50 110.5ms) / run611B 単発 1/20 (1216.4ms, warm p50 43.1ms) / run611C 単発 1/20 (1409.1ms, warm p50 40.3ms), landing control (kotobase.net/signup, 同時刻, n=20, 全 200) cold 0/20 p50 51.8ms max 77.5ms 完全静穏で control 分離成立 clean-tick。3時台 (9/14) 帯初 11/60 (~18.3%) は run578 (9/11) 10/60 (~16.7%) と同水準の同帯 2 日目実績 — run178A 型 heavy クラスタ (9/20) が 3時台でも再現し、深夜帯低位帯日次突発 (run557 1時台 11/60, run610 2時台 6/60 と連続) は K-Z4 低位帯日差方向の材料を積み増し。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現時刻帯 n 積み増し継続)。secret 不含 (curl + python3 stats のみ)。")

kz3_idx = [i for i, l in enumerate(lines) if l.startswith('| K-Z3 |')]
assert kz3_idx, 'K-Z3 row not found'
for i in kz3_idx:
    row = lines[i].rstrip('\n')
    assert not row.endswith(ev[-60:]), 'already appended'
    lines[i] = row + ev + '\n'

iter_idx = [i for i, l in enumerate(lines) if l.strip() == '## Iteration log']
assert len(iter_idx) == 1, f'iter header count {len(iter_idx)}'
entry = ("- 2026-09-14: falsify 第250回 (03:40 JST tick)。HEAD c4a4ceb = fetch 後 net-kotobase/main 先端一致 (乖離 0; detached HEAD のため fetch + rev-parse 比較手順)。rank 第267回 NEXT「K-Z3 3時台 run611」に従い production HTTP 実測で run611A-C を実施 (同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 03:42-03:44 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test; 本 tick 初手 kotobase.net/api/search は 404 (Not Found: /api/search) で 2 窓 120 試行を不採用別測定とし正 endpoint でやり直し): cold(>=0.5s) 9/1/1 per 20 = 11/60 (~18.3%) - run611A 散発クラスタ 9/20 (739-1406ms) / B 単発 1/20 / C 単発 1/20, control cold 0/20 p50 51.8ms max 77.5ms 完全静穏で分離成立 clean-tick。host load1 9.49 (3:44) は production HTTP 実測のため gate 外。3時台通算 (9/11 run578 10/60 + 9/14 本測 11/60) の同帯 2 日実績で run578 同水準 (~16.7% vs ~18.3%)。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現時刻帯 n 積み増し継続)。secret は一切記録せず (curl + python3 stats のみ)。\n")
lines.insert(iter_idx[0] + 1, entry)

with open(path, 'w', encoding='utf-8') as fh:
    fh.writelines(lines)

print('appended to rows', [i + 1 for i in kz3_idx], 'iter at', iter_idx[0] + 1)
