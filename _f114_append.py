INS = (" falsify 2026-09-06 (第114回, K-Z3 21時台 n 積み増し run251A–C, 同測定法 n=20 × 3 + landing control, "
       "別接続 curl, Tokyo, 21:48:45–21:49:47 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
       "host load1 110.72→148.72 (21:48/21:49 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 — "
       "rank 第109回 NEXT「K-Z3 22時台帯初計測」は 22時台だが cron 時刻 21:48 が21時台のため待機不可能、"
       "falsify 第88回/99/113回 precedent に従い 現在時刻帯 21時台 n 積み増しで実施; ※ run250 は bench 第101回使用済みのため run251): "
       "cold(>=0.5s) 3/2/1 per 20 = 6/60 (~10.0%) — run251A 散発 3 件 (1.3519s 1番目 / 1.6701s 5番目 / 0.6794s 11番目) p50 158.4ms warm_p50 126.8ms "
       "/ run251B 散発 2 件 (0.7129s 14番目 / 1.1460s 16番目) p50 152.8ms warm_p50 135.5ms / run251C 単発 1 件 (0.6075s 3番目) p50 126.0ms warm_p50 118.8ms, "
       "control (kotobase.net/signup) cold 0/20 p50 69.9ms max 479.1ms 静穏で control 分離成立、cold 群は search 側に局在。"
       "※本 tick は host load 急上昇 (110→149) tick で search warm p50 (119–136ms) と control p50 (69.9ms) が全体的上振れだが "
       "cold 6 件 (0.607–1.670s) は閾値決定的で cold 濃度判定 6/60 に影響なし (control max 479ms が閾値直下のため borderline 注記付き)。"
       "run251A/B/C の cold は各 run 内散発配置で「帯内散発単発即消失」パターン継続 — 21時台通算 (run245 3/60 + run246 1/60 + run247 1/60 + run248 2/60 "
       "+ run249 2/60 + bench run250 2/60 + 本 tick 6/60) 17/420 (~4.0%) 低位帯サンプル続く, 9/4 21時台 ~58% 記録の非再現が 7 セット続きで "
       "traffic 依存説の方向支持継続 (n=7 セット, 帯確定は rank 判定に委ねる)。status 判定は rank に委ねる (rank 専門)。")

path='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(path) as f:
    lines=f.readlines()
lines[242]=lines[242].rstrip('\n')+INS+'\n'
with open(path,'w') as f:
    f.writelines(lines)
print("APPENDED ok")