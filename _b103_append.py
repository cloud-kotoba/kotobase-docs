import io
path='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(path,encoding='utf-8').read().split('\n')
# K-Z3 cell is line index 254 (1-based 255)
idx=254  # 0-based line 255
line=lines[idx]
append_text = (
 " bench 2026-09-06 (第103回, K-Z3 22時台 n 積み増し run255A\u2013C — rank 第111回 NEXT「K-Z3 22時台追加 n 或 23時台帯初計測」の cron 時刻帯 22時台実施, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 22:38:25\u201322:39:52 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 97.57 (22:39 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外):"
 " cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run255A cold 2/20 (2.0938s 1番目 / 1.3073s 5番目, 冒頭散発) p50 168.7ms / run255B 0/20 p50 139.4ms max 276.6ms / run255C 0/20 p50 173.1ms max 305.0ms"
 " — control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 152.7ms max 254.0ms と search warm 同程度の上振れだが cold 0 で control 分離成立、cold 群は search 側に局在。"
 " run255A 冒頭散発 2 件は B/C 0/20 で即消失し run252A/253A 型 heavy burst の非再現・「帯内 1 窓即消失」単発散発型 (run254 同型)。"
 " ※本 tick は host load 97 高騰 tick で search p50 (139\u2013173ms) と control p50 (153ms) が quiet-tick の 40\u201360ms 帯から全体的に上振れしており warm 群上振れ込み (cold 濃度判定 2/60 自体は閾値決定的, borderline note)。"
 " 22時台通算は run252 (9/60 borderline) + bench run253 (6/60 clean-tick 分離成立) + run254 (2/60) + 本 tick (2/60) = 19/240 (~7.9%) — 21時台 (17/420 ~4.0%) と 9/5 22時台 (7/180 ~3.9%) より高位傾向を 4 セットで維持し、bench run253 (clean-tick) の 22時台高位再現を run254/255 が host load 高騰 tick で弱く追随 (run253 単独ではなく独立計測が続く点は夜帯高位の方向支持を弱める)。"
 " status 判定は rank に委ねる (rank 専門)。"
)
lines[idx]=line+append_text
open(path,'w',encoding='utf-8').write('\n'.join(lines))
print("appended run255 to K-Z3 cell, new cell chars:", len(lines[idx]))