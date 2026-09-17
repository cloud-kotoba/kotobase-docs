import re, datetime
doc='query-cosientist.md'
s=open(doc,encoding='utf-8').read()
anchor='## Iteration log\n'
i=s.find(anchor)
assert i>=0
entry='- 2026-09-13: falsify 第251回 (03:24 JST tick)。fetch 後 HEAD==net-kotobase/main 先端一致確認 (6998d2d, detached HEAD のため fetch + rev-parse 比較; git pull --ff-only は silent 失敗のため不使用手順)。rank 第264回 NEXT「K-Z3 3h clean-tick contrast」は本 tick が 3時台 tick で clean-tick 要件は rank 課題として残るが、production HTTP 実測は即時実施可能なため 3時台 n 積み増し run593A-C を実施 (同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 03:26-03:28 JST, 全 80/80 200): cold(>=0.5s) search 10/1/0 per 20 = 11/60 (~18.3%) — run593A 散発クラスタ 9/20 (0.78-1.83s) p50 81.0ms / run593B 単発 1/20 / run593C 0/20 p50 67.0ms, control cold 2/60 (0.68/0.71s 単発 2 窓) 非静穏で not-separated (search deep cold 10 件は magnitude 逆方向で search 側濃厚局在傾向)。23時台 run592 10/60 (~16.7%) に続き 3時台も中高位で深夜帯通しの高位方向を支持。host load1 8.72 (03:23 pre-tick 実測, gate 7.5 超過) は production HTTP 実測のため gate 外。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。secret 不含 (curl + python3 stats のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続, 次 run ID は run594 使用)。\n'
new=s[:i+len(anchor)]+entry+s[i+len(anchor):]
open(doc,'w',encoding='utf-8').write(new)
chk=open(doc,encoding='utf-8').read()
print('entrycount=',chk.count('falsify 第251回 (03:24 JST tick)'))
print('combining=',sum(1 for c in chk if 0x300<=ord(c)<=0x36F))
