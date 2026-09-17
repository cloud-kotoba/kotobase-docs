lines = open('query-cosientist.md').read().split('\n')

falsify_ev = (r" falsify 2026-09-06 (第111回, K-Z3 21時台帯初計測 run245A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 21:02:35–21:03:06 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 26.93 (pre-run 計測, gate 7.5 超過) は production HTTP 実測のため gate 外 — rank 第107回 NEXT「K-Z3 21時台帯初計測」に従い 21時台で実施): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run245A 散発 3 件 (1.0447s 8番目 / 1.2005s 10番目 / 1.9943s 13番目, warm 群 p50 55.6ms 静穏帯水準) p50 62.6ms / run245B cold 0/20 p50 103.7ms max 321.7ms / run245C cold 0/20 p50 57.6ms max 197.8ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 56.6ms max 137.4ms と静穏で control 分離成立、cold 群は search 側に局在。run245A 散発 3 件は B/C 0/20 で即消失し run241/243/244 型「帯内散発単発即消失」パターン継続 — 21時台帯初計測で cold 3/60 (~5.0%) は 20時台 (12/420 ~2.9%) と同水準、9/4 21時台 ~58% 記録との 2 日差対比は低位側で evening peak 後〜夜帯への遷移という traffic 依存説の方向支持に寄与 (n=1 帯初セットで確定はせず、深夜帯 ~26-31% 平坦パターンとの対比は不変)。status 判定は rank に委ねる (rank 専門)。"
)
lines[242] = lines[242].rstrip()
assert lines[242].endswith('status 判定は rank に委ねる (rank 専門)。'), lines[242][-40:]
lines[242] = lines[242] + falsify_ev

log_entry = r"- 2026-09-06: falsify 第111回。21:00 JST tick。fetch + rev-parse 比較で取り込み (HEAD 1cf582d = net-kotobase/main 先端一致, 乖離 0)。rank 第107回 NEXT「K-Z3 21時台帯初計測」に従い 21時台帯初計測 run245A–C を実施 (pre-run monitor の NEXT「23時台」は rank 第90回 stale と判断)。live smoke 200 (/, /signup; pre-run 計測)。host load1 26.93 (21:00 uptime 実測, gate 7.5 超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。K-Z3 run245A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 21:02:35–21:03:06 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run245A 散発 3 件 (1.0447/1.2005/1.9943s 8/10/13番目) p50 62.6ms warm_p50 55.6ms / run245B 0/20 p50 103.7ms max 321.7ms / run245C 0/20 p50 57.6ms max 197.8ms, control (kotobase.net/signup) cold 0/20 p50 56.6ms max 137.4ms 静穏で control 分離成立、cold 群は search 側に局在。run245A 散発 3 件は B/C 0/20 で即消失し「帯内散発単発即消失」パターン継続 — 21時台帯初計測 3/60 (~5.0%) は 20時台 (12/420 ~2.9%) と同水準、9/4 21時台 ~58% 記録との対比で低位側 (evening peak 後〜夜帯遷移という traffic 依存説の方向支持に弱く寄与, n=1 で確定せず)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。"
lines.insert(284, log_entry)

open('query-cosientist.md', 'w').write('\n'.join(lines))
print("OK inserted")