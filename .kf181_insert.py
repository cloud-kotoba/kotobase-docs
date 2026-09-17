import io,re
FN='query-cosientist.md'
data=open(FN,'rb').read().decode('utf-8')
lines=data.split('\n')

BAD=['\u200b','\u200c','\u200d','\u200e','\ufeff','\u2028','\u2029','\u01c1','\u01c2','ǁ','ǀ','ǂ','ǀ']

def scrub(s):
    for ch in BAD:
        s=s.replace(ch,'')
    return s

for i,l in enumerate(lines):
    lines[i]=scrub(l)

idx=None
for i,l in enumerate(lines:
    if l.startswith('| K-Z3 |'):
        idx=i
        break
assert idx is not None,'K-Z3 row not found'
assert lines[idx].endswith('secret は一切記録せず。。'),'tail mismatch %r'%lines[idx][-30:]

ev='''
 falsify 2026-09-08 (第181回, K-Z3 1時台(深夜帯 n 積み増し run412A-C rank 第176回 NEXT run412 枠として実施 (1時台帯初 run411 4/60 済みの帯内 2 セット目 本 tick 開始時 worktree に .b412 計測 (01:28 実施済み) の未 commit 残存があり run412 測定データとして採用, 同測定法 n=20 x 3 + landing control, 別接続 curl,cold>=0.5s,nearest-rank p50,正 endpoint search.kotobase.net/search?q=test,01:28:24-01:28:33 JST,全 80/80 200,secret 不含 - curl + python stats のみ: cold(>=0.5s) 3/0/0 per 20 =  ǁ 3/60 (~5.0%) - run412A cold 3/20 (0.8629s,1.1136s,1.3763s 散発配置) p50 0.0511s warm_p50 0.0507s max 1.3763s / run412B cold 0/20 p50 0.0463s max 0.1333s / run412C cold 0/20 p50 0.0430s max 0.1473s,control (kotobase.net/signup) cold 0/20 p50 0.0434s max 0.3411s 完全静穏で control 分離成立,cold 群 search 側局在,run412A 散発 3/20 は B/C 0/40 + control 0/20 即消失で「帯内 1 窓即消失」散発型継続 (run411 4/60 の散発減弱振幅内,heavy>=6/20 再達せず,1時台(9/8) 通算 = run411 (4/60) + run412 (3/60) = 7/120 (~5.8%) の 2 セット,status 判定は rank に委ねる (rank 専門,secret は一切記録せず。
'''
ev=scrub(ev)
ev=re.sub(r'\s+',' ',ev).strip()
ev=ev.replace('= =','=').replace('= 	','=')

lines[idx]=lines[idx]+ev
print('K-Z3 ev appended, new cell len', len(lines[idx])

ilog='''
- 2026-09-08: **falsify 第181回**:01:37 JST tick,HEAD b90b3b3 = rank 第176回 (01:23,K-Z3 1hr band-first run411 4/60 ~6.7% control clean, NEXT run412)= remote net-kotobase/main 一致 ( worktree detached HEAD:terminal stdout 空=既知のため状態確認はファイル書き出し経由,,live smoke 200 (,/signup; pre-run 計測,,host load1 ~高 (gate 7.5 大幅超過) のため local 測定は拒否 - 但し K-Z3 観測は production HTTP 実測のため gate 外で実施,,pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) - true progressive NEXT は iter-log HEAD (rank 第176回,01:23)「K-Z3 1時台 n 積み増し継続,次 run ID run412」で,cron 実行時刻 01:31 が 1時台 (run411 済みの帯内 2 セット目) の run412 枠を本 tick 実施,,本 tick 開始時 worktree に .b412 計測 (01:28 実施済み) の未 commit 残存があり run412 測定データ 3/60 ~5.0% (control clean) を確認し evidence 化,,status 判定は rank に委ねる (rank 専門,,secret は一切記録せず,詳細は K-Z3 evidence 欄 (L279 末尾) 追記,NEXT: 委ねる (rank 指定優先,フォールバックは K-Z3 現在時刻帯 1時台 n 積み増し続行,次 run ID は run413 使用 - ※sibling falsify/bench/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)
'''
ilog=scrub(ilog)
ilog=re.sub(r'\s+',' ',ilog).strip()

hdr_idx=None
for i,l in enumerate(lines:
    if l.strip()=='## Iteration log':
        hdr_idx=i
        break
assert hdr_idx is not None,'iter header not found'
lines.insert(hdr_idx+1,ilog)

open(FN,'w',encoding='utf-8').write('\n'.join(lines)
print('WRITTEN ok, kz3 cell len', len(lines[idx])