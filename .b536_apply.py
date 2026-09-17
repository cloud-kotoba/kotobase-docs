import sys
# bench 第242回 run536: append evidence to K-Z3 row + insert iter-log entry
EVIDENCE = (" bench 2026-09-09 (第242回, K-Z3 5時台 n 積み増し run536A–C — iter-log HEAD (bench 第241回, 05:00) NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 5時台 n 積み増し続行, 次 run ID は run536 使用)」の run536 枠, 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 05:10:44–05:11:02 JST, 全 80/80 200, host load1 87.96 (05:08 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 0/1/1 per 20 = 2/60 (~3.3%) — run536A cold 0/20 p50 0.1288s max 0.3129s / run536B 単発 1/20 (pos7 1.3310s) p50 0.1376s max 1.3310s / run536C 単発 1/20 (pos9 1.0925s) p50 0.1910s max 1.0925s, control (kotobase.net/signup) cold 1/20 (pos1 0.5314s 閾値直上境界値) p50 0.2009s max 0.5314s — host load 87 高騰の p50 全体的上振れ (search 129–191ms, control 201ms) 込みで control 分離は borderline not-separated-leaning, search 側 cold 2 件 (1.3310s/1.0925s) は閾値決定的で control 境界値単発とは独立。run536B/C 各単発は A 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (前 tick run535 完全静穏 0/60 から 1 窓のみの弱い再現, heavy>=6/20 は run271A 以降 42 セット連続非再現継続)。5時台 (9/9) 通算 = run535 (0/60) + 本 tick run536 (2/60) = 2/120 (~1.7%) の 2 セット — 前 tick 完全静穏から cold>0 へ弱い再現が一台あり 5時台も静穏低位帯水準を続行 (9/8 5時台 run421/423/424 0/60, 9/7 5時台 1/120 と整合方向)。深夜帯 traffic 最低帯の静穏方向に整合し K-Z3 traffic 依存説への強反証材料なし。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。")

ITER = "- 2026-09-09: bench 第242回。05:11 JST tick。HEAD 785c46d = bench 第241回 (05:00, K-Z3 5時台帯初 run535 cold 0/60 完全静穏) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第241回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 5時台 n 積み増し続行, 次 run ID は run536 使用)」)。本 tick は run536 を 5時台 n 積み増しとして実施。live smoke 200 (/, /signup, search; pre-run + 本 tick 実測 200)。host load1 87.96 (05:08 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。K-Z3 5時台 n 積み増し run536A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 05:10:44–05:11:02 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 0/1/1 per 20 = 2/60 (~3.3%) — run536A cold 0/20 p50 0.1288s max 0.3129s / run536B 単発 1/20 (pos7 1.3310s) p50 0.1376s max 1.3310s / run536C 単発 1/20 (pos9 1.0925s) p50 0.1910s max 1.0925s, control (kotobase.net/signup) cold 1/20 (pos1 0.5314s 閾値直上境界値) p50 0.2009s max 0.5314s — host load 87 高騰の p50 全体的上振れ込みで control は borderline not-separated-leaning, search 側 cold 2/60 自体は閾値決定的 (1.33s/1.09s)。4時台 16/240 ~6.7% から 5時台へ移行後も run535 完全静穏 0/60 → 本 tick 2/60 へ cold>0 一台継続 = K-Z3 traffic 依存説への反証材料を弱く継続 (深夜帯 ~26-31% 平坦パターンと整合方向, 5時台は静穏低位帯)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 5時台 n 積み増し続行, 次 run ID は run537 使用 — run531..536 消費済みのため次セットは run537)。"

src = '/tmp/bc_qc_head.md'
data = open(src, 'r', encoding='utf-8').read()

# find K-Z3 row line
lines = data.split('\n')
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 | worker |'):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'
row = lines[kz3_idx].rstrip()
if not row.endswith('|'):
    lines[kz3_idx] = row + EVIDENCE
else:
    lines[kz3_idx] = row[:-1] + EVIDENCE + '|'

new = '\n'.join(lines)
hdr = '## Iteration log'
assert hdr in new, 'iter log header not found'
new = new.replace(hdr, hdr + '\n' + ITER, 1)

out = '/tmp/bc_work_out.md'
with open(out, 'w', encoding='utf-8') as f:
    f.write(new)
print('OK kz3_idx=%d bytes=%d' % (kz3_idx, len(new.encode('utf-8'))))