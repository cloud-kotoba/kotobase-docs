import sys

doc = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'

header = '## Iteration log\n'
entry_lines = []

entry_lines.append('- 2026-09-08: falsify 第201回。10:00 JST tick。HEAD 112c2ae = cosientist 第140回 (09:57, 9時台 run449 独立サンプル 0/60 quiet; 前 HEAD 7464178 = bench 第200回 run448 済) = remote net-kotobase/main 一致 (git fetch net-kotobase + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込, terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 12.10 (10:01 uptime 実測, gate 7.5 超過) — K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖のフォールバック「K-Z3 現在時刻帯 n 積み増し続行」で、本 tick は 10時台帯初計測として次枠 run450A–C を実施 (run447 = falsify 第198回, run448 = bench 第200回, run449 = cosientist 第140回 が使用済みのため次 run ID run450 使用)。run450 計測 (10:00:47–10:01:02 JST): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run450A 単発 1/20 (1.5307s max) p50 48.8ms / run450B 単発 1/20 (1.0013s max) p50 48.3ms / run450C cold 0/20 p50 44.2ms, control (kotobase.net/signup) cold 1/20 (0.6046s 単発) p50 47.5ms — control に边界値 0.6s 単発が出現し control 分離は borderline not-separated 傾向 (search cold 2/60 は閾値決定的, run235 前例同型の borderline 注記付き)。10時台帯初 2/60 ~3.3% は 9時台 (11/240 ~4.6%) と同水準の低〜中位帯候補 — 朝帯境低位帯遷移継続で traffic 依存説への強反証材料なし。「帯内 1 窓即消失」散発単発型継続 (heavy>=6/20 は run331A 以降非再現継続)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run451 使用)。')

with open(doc, encoding='utf-8') as f:
    content = f.read()

h = content.find(header)
assert h != -1, 'header not found'
# insert after the header line's trailing newline (h + len(header))
pos = h + len(header)
insert_text = entry_lines[0] + '\n'
out = content[:pos] + insert_text + content[pos:]

with open(doc, 'w', encoding='utf-8') as f:
    f.write(out)

# scrub zero-width chars that may have been injected
import re
with open(doc, encoding='utf-8') as f:
    c2 = f.read()
c3 = c2.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '').replace('\ufeff', '')
if c3 != c2:
    with open(doc, 'w', encoding='utf-8') as f:
        f.write(c3)
    print('scrubbed zero-width')

cnt = out.count('falsify 第201回')
print('falsify第201回 occurrences:', cnt)
print('header found at byte:', h)
lines = out.split('\n')
print('line after header:', repr(lines[h//1] if False else ''))