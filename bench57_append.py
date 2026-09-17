D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
p=D+'/query-cosientist.md'
src=open(p).read()

EV=" bench 2026-09-05 (第57回, K-Z3 20時台 n 積み増し run168A–C — NEXT 委ねるのフォールバック, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 20:14:56–20:15:07 JST, 全 80/80 200, host load1 7.22 (tick 測定開始時, 1/5/15min 7.22/25.88/40.77, 5/15min は前 tick 遺残) は production HTTP 実測のため gate 外): run168A cold(>=0.5s) 4/20 (0.884s 2番目, 1.083s 5番目, 1.057s 14番目, 1.182s 16番目 — 散発配置) p50 0.054s / run168B cold 0/20 p50 0.042s (max 0.072s) / run168C cold 0/20 p50 0.050s (max 0.095s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.091s (max 0.141s) と静穏で control 分離成立、cold 群は search 側に局在。run168A は run89A 型の薄い cold 単独クラスタ (warm p50 上振れを伴わない) で B/C で即消失。20時台通算は 2026-09-04 run89–91 (4/180) + falsify run167 (0/60) + 本 tick で 8/300 (~2.7%) の低位帯。※ run167 は falsify 第63回 (同 tick 20:13 JST, 別インスタンス) と ID 衝突 — 本計測を run168 として読み替えて記録 (run105/run123/run124/run161 前例に従う)。status 判定は rank に委ねる (rank 専門)。"

lines=src.split('\n')
i=205
l=lines[i].rstrip()
assert l.startswith('| K-Z3 |')
assert l.endswith('継続)。'), 'unexpected tail: %r' % l[-30:]
lines[i]=l+" "+EV

LOG="- 2026-09-05: bench 第57回。rank 第56回 NEXT「委ねる」のフォールバック (K-Z3 現在時刻帯 n 積み増し) を受け、K-Z3 20時台 n 積み増し run168A–C を同測定法で実施 (20:14 JST, production HTTP 実測のため gate 外, secret 不含, host load1 7.22): search cold(>=0.5s) 4/60 (~6.7%, 0.884–1.182s 散発 4 件が run168A のみ, B/C は cold 0 で p50 42–50ms), landing control cold 0/20 p50 91ms と静穏で control 分離成立 — run168A は run89A 型薄い cold 単独クラスタで即消失。20時台通算 (2026-09-04 run89–91 + falsify run167 + 本 tick) 8/300 ~2.7% 低位帯。※ run167 は falsify 第63回 (同 tick 20:13 JST, cold 0/60) と ID 衝突 — 前例に従い本分を run168 として記録。status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。"
lines.append(LOG)
open(p,'w').write('\n'.join(lines))
print('appended')
