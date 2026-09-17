#!/usr/bin/env python3
import re
path='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s=open(path,encoding='utf-8').read()

def scrub(t):
    out=t.replace('\u200b','').replace('\u200c','').replace('\u200d','').replace('\ufeff','')
    out=out.replace('\xa0',' ')
    return out

ev=scrub(" falsify 2026-09-08 (第195回, K-Z3 8時台帯内 3セット目 run440A\u2013C — rank 第193回 NEXT\u300cK-Z3 8hr n-add run439\u300dの run439 枠は bench 第194回が試行のみ (DNS 解不能, 実測なし) のため run440 に読替 (run216/run256/run263/run278 precedent), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 08:19:30\u201308:19:42 JST, 全 80/80 200, host load1 49.89 (08:19 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/1/0 per  ̈20 =̈ 2/60 (~3.3%) — run440A 単発 1.439s / run440B 単発 1.122s / run440C 0/20, control (kotobase.net/signup) cold 0/20 p50 59.0ms max 139.6ms 完全静穏で control 分離成立,cold 群は search 側に局在。run440A/B 各単発は各 run 内即消失し\u300c帯内 1 窓即消失\u300d散発単発型継続 (heavy>=6/20 は run413A 以降非再現継続)。8時台 (9/8) 通算 = bench-run437 (cold 2/60,帯初) + falsify-run438 (cold 1/60) +本 tick run440 (cold 2/60) =受 5/180 (~2.8%) の 3 セット低位帯継続 — 5/6時台 完全静穏 と 7時台 8/360 ~2.2% に続く朝帯境低位帯の遷移継続で 深夜帯→朝帯境静穏方向に整合し, 23時台前回帯 (~5.2%) の 深夜帯 ~26-31% 平坦パターンとの対比は traffic 依存説の方向支持を維持。status 判定は rank に委ねる (rank 専門。)")

il=scrub("- 2026-09-08: falsify 第195回: 08:16 JST tick, HEAD 6ecd75b = bench 第194回 (08:10, K-Z3 8時台 n-add run439 試行— DNS 解不能で実測不能; NEXT run440) = remote net-kotobase/main 一致 ( git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込, terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 49.89 (08:19 uptime 実測, gate  ̈7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP釈実測 (同測定法 n=20 x 3 + landing control,別接続 curl, cold>=0.5s,正 endpoint search.kotobase.net/search?q=test, 全 80/80 200, secret 不含 — curl + python stats のみ) で run440A-C を実施: cold(>=0.5s) 2/60 (~3.3%) — run440A 単発 1/20 (1.439s) / run440B 単発 1/20 (1.122s) / run440C 0/20,,, control (kotobase.net/signup) 0/20 完全静穏分離成立,cold 群 search 側局在,\u300c帯内 1 窓即消失\u300d散発単発型継続。8時台 (9/8) 通算 = bench-run437 (帯初 2/60) + falsify-run438 (1/60) + 本 tick run440 (2/60) =受 5/180 (~2.8%) 低位帯継続 — 朝帯境低位帯 (5-7時台 低温帯) 継続で深夜帯→朝帯境静穏方向に整合し traffic 依存説への強反証材料なし,帯水準確定・機構判断は rank 追加 n 待ち。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先;フォールバックは K-Z3 現在時刻帯 8時台 n 積み増し続行,次 run ID は run441 使用。)")

#1. evidence append: find K-Z3 hypothesis row, append at end of that row(before its trailing \n)
key='| K-Z3 | worker |'
i=s.find(key)
if i<0:
    raise SystemExit('K-Z3 row not found')
nl=s.find('\n',i)
if nl<0:
    raise SystemExit('no newline after K-Z3 row')
s=s[:nl]+ev+s[nl:]

#2. iter-log insert after header line
hdr='\n## Iteration log\n'
j=s.rfind('\n## Iteration log\n')
if j<0:
    raise SystemExit('iter log header not found')
ins_pos=j+len('\n## Iteration log\n')
s=s[:ins_pos]+il+'\n'+s[ins_pos:]
open(path,'w',encoding='utf-8').write(s)
print('OK inserted')