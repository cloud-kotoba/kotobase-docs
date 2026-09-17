# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'

log_line = (
"- 2026-09-06: falsify 第102回。18:45 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse で同期確認 "
"(HEAD 64dfa22 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。rank 第98回 NEXT「K-Z3 現在時刻帯 18時台 n 積み増し継続」に従い 18時台で実施 "
"(host load1 80.91–97.20, gate 7.5 大幅超過だが production HTTP 実測のため gate 外)。live smoke 200 (/, /signup; pre-run 計測)。"
"K-Z3 run233A–C n 積み増し (同測定法 n=20 × 3 + landing control, 18:46:37–18:47:41 JST, 全 80/80 200, "
"正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 2/2/1 per 20 = 5/60 (~8.3%) — "
"run233A cold 2/20 (0.943s/0.792s) warm_p50 85.2ms / run233B cold 2/20 (0.764s/0.775s) warm_p50 137.1ms / "
"run233C cold 1/20 (1.310s) warm_p50 114.8ms, control (kotobase.net/signup) cold 2/20 (0.999s/0.789s) p50 271.7ms — "
"search/control とも warm p50 全体的上振れ + control に cold 2 件出現で control 分離は borderline not-separated "
"(host load 高騰 97 tick の一般化遅延と整合、実在 cold-start 特有とは判定不能)。18時台通算 18/240 (~7.5%) に上振れ、"
"run232A 単一窓 heavy に加え本 tick 3 run 跨ぎ弱連続 cold で「帯内1窓即消失」パターンは 18時台では成立せず "
"低位帯から中間帯への弱い遷移方向 (load 高騰混入で決定的でない)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n"
)

s = open(PATH, encoding='utf-8').read()
anchor = '## Iteration log\n'
assert s.count(anchor) == 1, f"anchor count={s.count(anchor)}"
# insert log_line immediately after the anchor line
s = s.replace(anchor, anchor + log_line, 1)
open(PATH, 'w', encoding='utf-8').write(s)
print("OK inserted log entry")