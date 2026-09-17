import io

SRC='/tmp/qc_head.md'
DST='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'

with io.open(SRC,encoding='utf-8') as f:
    text=f.read()

iter_entry = (
"- 2026-09-09: bench 第247回。10:00 JST tick (計測 10:0x JST, HEAD 78c6404 = falsify 第241回 (09:53, K-Z3 9時台 run543 cold 3/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル書出経由))。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (falsify 第241回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run544 使用 - run538..543 消費済みのため次セットは run544)」)。本 tick は 現時刻帯 9時台 (9/9) n 積み増し (7 セット目) run544 を実施。live smoke 200 (/, /signup, search; 本 tick 実測 200)。host load1 ~91->128 (09:53-10:11 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。K-Z3 9時台 run544A-C 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 10:00-10:01 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) - run544A 単発 1/20 (pos6 1.2170s) p50 0.1986s max 1.2170s / run544B cold 0/20 p50 0.1686s max 0.4981s / run544C cold 0/20 p50 0.1351s max 0.4515s, control (kotobase.net/signup) cold 0/20 p50 0.1866s max 0.2804s 完全静穏で control 分離成立, cold 群 search 側局在,「帯内 1 窓即消失」散発単発型継続 (falsify run543B/C 冒頭散発 2/20 の ~7 分後減衰, heavy>=6/20 非再現継続)。9時台 (9/9) 通算 = run538 (0/60) + run539 (0/60) + run540 (4/60) + run541 (0/60) + run542 (1/60) + run543 (3/60) + 本 tick run544 (1/60) = 9/420 (~2.1%) の 7 セット - 朝帯静穏低位帯候補方向に整合継続 (5時台 ~2.8% と同水準, K-Z3 traffic 依存説への強反証材料なし)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run545 使用 - run538..544 消費済みのため次セットは run545)。"
)

# Inline evidence appended directly to K-Z3 row-line END (row.rstrip()), NO leading newline
ev_text = (
" bench 2026-09-09 (第247回, K-Z3 9時台 n 積み増し run544A-C - falsify 第241回 (09:53, run543) に続く 9時台 (9/9) 7 セット目, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 10:00-10:01 JST, 全 80/80 200, host load1 ~91-128 (09:53-10:11 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) - run544A 単発 1/20 (pos6 1.2170s) p50 0.1986s max 1.2170s / run544B cold 0/20 p50 0.1686s max 0.4981s / run544C cold 0/20 p50 0.1351s max 0.4515s, control (kotobase.net/signup) cold 0/20 p50 0.1866s max 0.2804s 完全静穏で control 分離成立, cold 群 search 側局在,「帯内 1 窓即消失」散発単発型継続 (falsify run543 散発 3/60 の ~7 分後減衰, heavy>=6/20 非再現継続)。9時台 (9/9) 通算 = run538 (0/60) + run539 (0/60) + run540 (4/60) + run541 (0/60) + run542 (1/60) + run543 (3/60) + 本 tick run544 (1/60) = 9/420 (~2.1%) の 7 セット - 朝帯静穏低位帯候補方向に整合継続 (5時台 ~2.8% と同水準, K-Z3 traffic 依存説への強反証材料なし)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。"
)

kz3 = '| K-Z3 |'
kid = text.find(kz3)
if kid < 0:
    raise SystemExit('K-Z3 row not found')
eol = text.find('\n', kid)
if eol < 0:
    raise SystemExit('no newline after K-Z3 row')
# concatenate ev_text directly at end of row line (before the newline)
new_kz3 = text[:eol] + ev_text + text[eol:]
text = new_kz3

hdr = '## Iteration log\n'
hid = text.find(hdr)
if hid < 0:
    raise SystemExit('iter header not found')
insert_at = hid + len(hdr)
text = text[:insert_at] + iter_entry + '\n' + text[insert_at:]

with io.open(DST,'w',encoding='utf-8') as f:
    f.write(text)
print('OK inserted inline')