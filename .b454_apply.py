import io
MD='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with io.open(MD, encoding='utf-8') as f:
    text = f.read()
    ls = text.split('\n')

evidence = (" bench 2026-09-08 (第202回, K-Z3 10時台 n 積み増し run454A-C — iter-log HEAD "
"(falsify 第203回 run453, 10:34) NEXT「K-Z3 現在時刻帯 10時台 n 積み増し続行, 次 run ID は run454 使用」"
"の run454 枠として実施 (10時台 5セット目, run453 済みの積み増し続行, .b454 既存なし=衝突なし確認), "
"同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
"正 endpoint search.kotobase.net/search?q=test, 10:40:55-10:41:03 JST, 全 80/80 200, "
"host load1 9.43 (10:40 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, "
"secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — "
"run454A cold 単発散発 1.086s (pos9) p50 52.2ms / run454B cold 単発散発 1.454s (pos7) p50 47.2ms / "
"run454C cold 0/20 p50 43.0ms, control (kotobase.net/signup) cold 0/20 p50 41.7ms max 132.9ms "
"完全静穏で control 分離成立、cold 群は search 側に局在。run454A/B 各単発は C 0/20 + control 0/20 "
"で即消失し「帯内 1 窓即消失」散発単発型継続 (run453A 散発クラスタ 4/20 は 6 分後の本 tick 2/60 に減衰、"
"heavy>=6/20 は run331A 以降非再現継続)。10時台 (9/8) 通算 = falsify run450 (2/60) + bench run451 (2/60) "
"+ falsify run452 (2/60) + falsify run453 (5/60) + 本 tick run454 (2/60) = 13/300 (~4.3%) "
"の 5 セット連続 cold>0 — 9時台 (11/300 ~3.7%) と同水準の低〜中位帯候補、traffic 依存説への強反証材料なし。"
"status 判定は rank に委ねる (rank 専門)。")

iter_entry = ("- 2026-09-08: bench 第202回。10:41 JST tick。HEAD 653e162 = falsify 第203回 "
"(10:34, K-Z3 10時台 n-add run453 cold 5/60 ~8.3% control borderline) = remote net-kotobase/main 一致 "
"(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込, "
"terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。"
"live smoke 200 (/, /signup; pre-run 計測 + 本 tick 実測 search/signup 200)。"
"host load1 9.43 (10:40 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は "
"production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 "
"n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD "
"(falsify 第203回, 10:34)「K-Z3 現在時刻帯 10時台 n 積み増し続行, 次 run ID は run454 使用」の run454 枠を "
"本 tick 実施 (10時台 5セット目, falsify 第203回 run453 済みの積み増し続行, .b454 既存なし=衝突なし確認)。"
"run454 計測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
"正 endpoint search.kotobase.net/search?q=test, 10:40:55-10:41:03 JST, 全 80/80 200): "
"cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run454A cold 単発散発 1.086s (pos9) p50 52.2ms / "
"run454B cold 単発散発 1.454s (pos7) p50 47.2ms / run454C cold 0/20 p50 43.0ms, "
"control (kotobase.net/signup) cold 0/20 p50 41.7ms max 132.9ms 完全静穏で control 分離成立、"
"cold 群は search 側に局在。run454A/B 各単発は C 0/20 即消失で「帯内 1 窓即消失」散発単発型継続 "
"(run453A 散発クラスタ 4/20 は 6 分後の本 tick 2/60 に減衰、heavy>=6/20 非再現継続)。10時台 (9/8) 通算 "
"= run450 (2/60) + run451 (2/60) + run452 (2/60) + run453 (5/60) + 本 tick run454 (2/60) = "
"13/300 (~4.3%) の 5 セット連続 cold>0 — 9時台 (11/300 ~3.7%) と同水準の低〜中位帯候補、"
"traffic 依存説への強反証材料なし。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
"status 判定・帯水準確定・機構判断は rank に委ねる (rank 専門)。secret は一切記録せず。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 10時台 n 積み増し続行, 次 run ID は run455 使用)。")

# --- apply row append: find K-Z3 hypothesis row by leading token ---
kz_idx = None
for i, l in enumerate(ls):
    if l.startswith('| K-Z3 |'):
        kz_idx = i
        break
assert kz_idx is not None, 'K-Z3 row not found'
# append evidence to row end (row does not end with '|')
ls[kz_idx] = ls[kz_idx] + ' ' + evidence

# --- apply iter-log insert: find first '## Iteration log' header ---
hdr_idx = None
for i, l in enumerate(ls):
    if l.strip() == '## Iteration log':
        hdr_idx = i
        break
assert hdr_idx is not None, 'iter log header not found'
insert_at = hdr_idx + 1
ls[insert_at:insert_at] = [iter_entry]

out_text = '\n'.join(ls)
with io.open(MD, 'w', encoding='utf-8') as f:
    f.write(out_text)
with io.open('/tmp/bk_apply_log.txt','w',encoding='utf-8') as f:
    f.write('kz_row_idx=%d\n' % kz_idx)
    f.write('iter_hdr_idx=%d insert_at=%d\n' % (hdr_idx, insert_at))
    f.write('new line count=%d\n' % len(ls))
print('applied')