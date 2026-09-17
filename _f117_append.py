p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
INS = " falsify 2026-09-06 (第117回, K-Z3 22時台 n 積み増し run256A-C — 本 tick 22:47 JST, run255 (bench 第103回) の次の空き ID, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 22:47:36–22:48:00 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 28.12→24.15 (22:47/22:48 uptime 実測, gate 7.5 超過だが production HTTP 実測のため gate 外, tick 開始時 62–85 から測定中に低下), secret 不含 — curl のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run256A cold 2/20 (1.193s, 2.011s, 散発ペア) p50 48.9ms / run256B cold 0/20 p50 52.1ms / run256C cold 0/20 p50 46.5ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 57.4ms max 111ms と control 分離成立、cold 群は search 側に局在 (散発ペア型)。本 tick は host load が tick 開始 (22:45 時点 62–85) から測定中に 24 まで低下して温まり、search p50 (47–52ms) も control p50 (57ms) も quiet-tick の 40–60ms 帯に復帰しており 22時台 clean-tick 分離の再現 (前 tick bench run255 の host load 高騰 not-separated とは異なり本 tick は分離成立)。22時台通算は run252 (9/60) + bench run253 (6/60) + run254 (2/60) + bench run255 (2/60) + 本 tick run256 (2/60) = 21/300 (~7.0%) で、21時台 (bench run243-245 等 17/420 ~4.0%) より高位を維持し、22時台の散発 cold が継続的に再現される点は夜帯 traffic 遷移説を弱い方向支持。status 判定は rank に委ねる (rank 専門)"
lines=open(p,encoding='utf-8').readlines()
lines[254]=lines[254].rstrip('\n')+INS+"\n"
open(p,'w',encoding='utf-8').write("".join(lines))
cnt=open(p,encoding='utf-8').read().count("run256")
with open('/tmp/f117_ins.txt','w',encoding='utf-8') as f:
    f.write("run256 occurrences: %d\n" % cnt)
print("OK run256 occ=%d" % cnt)