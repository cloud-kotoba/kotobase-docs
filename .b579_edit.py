import io
p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
# K-Z3 row: two physical lines share the hypothesis text; target the one with latest evidence (run578)
idx = [i for i, l in enumerate(lines) if l.startswith('| K-Z3 |') and 'run578' in l]
assert len(idx) == 1, idx
i = idx[0]
ev = '  falsify run579A-C (9/11 11時台 2セット目, 11:24-11:25 JST, n=20 x3 + landing control, 別接続 curl, Tokyo, 全 80/80 200): cold(>=0.5s) 0/60 - A p50 37.8ms max 396.8ms / B p50 37.0ms max 372.4ms / C p50 37.1ms max 489.8ms, control 0/20 p50 45.7ms max 197.9ms 完全静穏で control 分離成立。同帯同日 run578 (bench 第217回) 10/60 (~16.7%) から本セット 0/60 へ窓内即消失 - 11時台 9/11 通算 10/120 (~8.3%), 散発単発クラスタ型継続。host load1 57-83 (gate 7.5 超過) は production HTTP 実測のため gate 外。status 判定は rank に委ねる (rank 専門)。'
assert 'run579' not in lines[i], 'dup check'
lines[i] = lines[i].rstrip() + ev
# iter log insert after header
hi = lines.index('## Iteration log')
entry = '- 2026-09-11: falsify 第248回 (11:23 JST tick)。HEAD 6144aa4 = fetch 後 net-kotobase/main 先端一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 手順; terminal foreground stdout 空=既知のため状態確認はファイル書出経由)。bench 第217回 run578 (11:07, 11時台 9/11 分) 済みのためフォールバック (production HTTP 実測) で K-Z3 11時台 2セット目 n 積み増し run579A-C を実施 (同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 11:24-11:25 JST, 全 80/80 200): cold(>=0.5s) 0/60 - run579A p50 37.8ms max 396.8ms / run579B p50 37.0ms max 372.4ms / run579C p50 37.1ms max 489.8ms, control (kotobase.net/signup) cold 0/20 p50 45.7ms max 197.9ms 完全静穏で control 分離成立。同帯同日 run578 10/60 (~16.7%) から本セット 0/60 - 「帯内 1 窓即消失」散発単発型。11時台 9/11 通算 10/120 (~8.3%) (9/9 ~1.7%, 9/10 ~16.7% と合わせ K-Z4 候補 日差材料)。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。K-Q1 (cacao_b64 harness 変更) は host load gate 大幅超過 (load1 57-83) のため本 tick も実施せず, 次の低負荷 tick 待ち。secret 不含 (curl + python3 stats のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 12時台 (9/11) n 積み増し)。'
lines.insert(hi + 1, entry)
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('OK', len(lines))
